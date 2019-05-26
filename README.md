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

`` ` python INSTALLED_APPS = (     ...     'toad',     ... ) ```

Add hackoregon_transportation_systems's URL patterns:

`` ` python from hackoregon_transportation_systems.toad import urls as toad_urls   urlpatterns = [     ...     url(r'^', include(toad_urls)),     ... ] ```

Setup your database with a matching schema

Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Local development workflow
1. Clone this repository. For the moment, everything is still in the
branch `create-local-database-container`, so check out that branch.
2. Open a command terminal. Copy the file `env.sample` to `.env'.
Change the passwords if you want to - that's really not necessary
since the listeners are all on your workstation / laptop. But do
it anyway to get into the habit.
3. Copy the `tadpole.backup` file into `Backups/`. This is a small
version (just September 2017 and September 2018) of our TOAD data.
4. Make sure your Docker host is working and has plenty of space.
This dataset requires at least 11 GB. On my machines the Docker
volume space lives on 128 GB SSDs so I have to watch this stuff.
If you're on Windows or a Mac this will be in a virtual disk somewhere.
5. Open a command prompt and type `bin/build.sh -l`. This will build
the images. Open an issue if it doesn't work.
6. Type `bin/start.sh -l`. The containers will start up. The database
restore takes quite a bit of time; you'll see the API container polling
it every five seconds. That's annoying; I should change it to every
minute. ;-)
7. When the database comes up, the API container will run a bunch of
stuff and then start a server. You should see the Django success page
at http://localhost:8000.
8. There's a pgAdmin4 container listening on http://localhost:8686.
If you want to use it, browse there. First log in to pgAdmin4 with
the email address and password you set in `.env`. Then right-click
on `Servers`. You'll see `local_postgis`; that's the local database
container. When you click on that, it will ask you for a password.
That's `POSTGRES_PASSWORD` from the `.env` file - copy and paste.

# Credits

Tools used in rendering this package:

> -   [Cookiecutter](<https://github.com/audreyr/cookiecutter>)
> -   [cookiecutter-djangopackage](<https://github.com/pydanny/cookiecutter-djangopackage>)
