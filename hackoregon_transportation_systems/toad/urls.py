from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()


#schema view
schema_view = get_swagger_view(title='Transportation Systems 2019 API')

urlpatterns = [
    url(r'^schema/', schema_view),
    url
    url(r'^toad/', include(router.urls)),
]
