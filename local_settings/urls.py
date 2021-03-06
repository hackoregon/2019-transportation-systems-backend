from django.conf.urls import include, url
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()


class JSONOpenAPIRender(renderers.OpenAPIRenderer):
    media_type = "application/json"


def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
    """
    Returns schema view which renders Swagger/OpenAPI.
    """

    class SwaggerSchemaView(APIView):
        _ignore_model_permissions = True
        exclude_from_schema = True
        permission_classes = [AllowAny]
        renderer_classes = [
            CoreJSONRenderer,
            JSONOpenAPIRender,
            renderers.OpenAPIRenderer,
            renderers.SwaggerUIRenderer,
        ]

        def get(self, request):
            generator = SchemaGenerator(
                title=title, url=url, patterns=patterns, urlconf=urlconf
            )
            schema = generator.get_schema(request=request)

            if not schema:
                raise exceptions.ValidationError(
                    "The schema generator did not return a schema Document"
                )

            return Response(schema)

    return SwaggerSchemaView.as_view()


schema_view = get_swagger_view(title="Hack Oregon Transportation Systems 2019 API")


urlpatterns = [
    url(r"^transportation2019/v1/schema/", schema_view),
    url(
        r'^transportation2019/v1/docs/',
        include_docs_urls(title="Hack Oregon Transportation Systems 2019 API")
    ),
    url(
        r"^transportation2019/v1/toad/",
        include("hackoregon_transportation_systems.toad.urls"),
    ),
]
