#! /bin/bash

# wait-for-postgres.sh
# https://docs.docker.com/compose/startup-order/

# http://linuxcommand.org/lc3_man_pages/seth.html:
# -e  Exit immediately if a command exits with a non-zero status.
set -e

# Pull in environment variables values from AWS Parameter Store, and preserve the exports
# source usage per https://stackoverflow.com/q/14742358/452120 (iff running on travis-ci)


if [ -z ${DEBUG+x} ]; then echo "DEBUG var is unset, setting to False" && export DEBUG=false ; else echo "var is set to '$DEBUG'"; fi
if [ -z ${TRAVIS+x} ]; then echo "TRAVIS var is unset, setting to False" && export TRAVIS=false ; else echo "var is set to '$TRAVIS'"; fi

echo DEBUG: "${DEBUG}"
echo DEBUG,,: "${DEBUG,,}"
echo TRAVIS: "${TRAVIS}"
echo TRAVIS,,: "${TRAVIS,,}"

#if [ ! "${DEBUG}" ] && [ ! "${TRAVIS}" ]; then
  source /code/bin/get-ssm-parameters.sh
  echo POSTGRES_NAME: "${POSTGRES_NAME}"
  echo POSTGRES_HOST: "${POSTGRES_HOST}"
  echo POSTGRES_PORT: "${POSTGRES_PORT}"
#fi

chmod +x *.py

echo "Make migrations"
python -Wall manage.py makemigrations toad

echo "Migrate"
python -Wall manage.py migrate

# Collect static files
echo "Collect static files"
python -Wall manage.py collectstatic --noinput

echo "Run server..."
gunicorn backend.wsgi -c gunicorn_conf.py
