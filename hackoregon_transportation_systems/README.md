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

# Quickstart to install package in your own Django Project (Non-Hack
Oregon Workflow)

Install hackoregon_transportation_systems:

> pip install hackoregon_transportation_systems

Add subpackages to your `INSTALLED_APPS`:

``` python INSTALLED_APPS = (     ...     'toad',     ... ) ```

Add hackoregon_transportation_systems's URL patterns:

``` python from hackoregon_transportation_systems.toad import urls as toad_urls   urlpatterns = [     ...     url(r'^', include(toad_urls)),     ... ] ```

Setup your database with a matching schema

Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Credits

Tools used in rendering this package:

> -   [Cookiecutter](<https://github.com/audreyr/cookiecutter>)
> -   [cookiecutter-djangopackage](<https://github.com/pydanny/cookiecutter-djangopackage>)
