|
--------------------------------------------- |
hackoregon_transportation_systems |

[![image](<https://badge.fury.io/py/>2019-transportation-systems-backend.svg)](<https://badge.fury.io/py/>2019-transportation-systems-backend)

[![image](<https://travis-ci.org/hackoregon/>2019-transportation-systems-backend.svg?branch=master)](<https://travis-ci.org/hackoregon/>2019-transportation-systems-backend)

2019 Transportation Systems APIs

# Documentation

The full documentation is at <<http://hackoregon.github.io/>>2019-transportation-systems-backend

# Features

> -   TODO (add what your project does)

# Data Sources

# Quickstart to install package in your own Django Project (Non-HackOregon Workflow)

Install hackoregon_transportation_systems:

> pip install hackoregon_transportation_systems

Add subpackages to your `INSTALLED_APPS`:

```python 
INSTALLED_APPS = (     ...     'toad',     ... ) 
```

Add hackoregon_transportation_systems's URL patterns:

```python 
from hackoregon_transportation_systems.toad 
import urls as toad_urls   
urlpatterns = [     ...     url(r'^', include(toad_urls)),     ... ] 
```

Setup your database with a matching schema

Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Local development workflow
1. Clone this repository.
2. Open a command terminal. Copy the file `env.sample` to `.env`.
Update the `.env` file with the proper RDS credentials.
3. Make sure your Docker host is working.
4. Open a command prompt and type `./scripts/build-run/build.sh -d`. This will build
the images. Open an issue if it doesn't work. NOTE: This command (and the one below) runs `sudo` in the background, so you will likely be asked for your log-in password to provide permission to begin. Don't confuse this with the passwords defined in the `.env` file.
5. Type `./scripts/build-run/start.sh -d`. The containers will start up.
6. When the database comes up, the API container will run a bunch of
stuff and then start a server. You should see the Django success page
at http://localhost:8000. (You may need to navigate to http://lhttp://localhost:8000/transportation2019/v1/schema/).


# Credits

Tools used in rendering this package:

> -   [Cookiecutter](<https://github.com/audreyr/cookiecutter>)
> -   [cookiecutter-djangopackage](<https://github.com/pydanny/cookiecutter-djangopackage>)
