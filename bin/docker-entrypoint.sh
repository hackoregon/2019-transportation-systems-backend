#! /bin/bash

# wait-for-postgres.sh
# https://docs.docker.com/compose/startup-order/

# http://linuxcommand.org/lc3_man_pages/seth.html:
# -e  Exit immediately if a command exits with a non-zero status.
set -e

# Pull in environment variables values from AWS Parameter Store, and preserve the exports
# source usage per https://stackoverflow.com/q/14742358/452120 (iff running on travis-ci)


if [ -z ${DEBUG+x} ]; then echo "DEBUG var is unset, setting to False" && export DEBUG=false ; else echo "var is set to '$DEBUG'"; fi

echo Debug: "${DEBUG,,}"

if [ ! "${DEBUG,,}" ] && [ ! "${TRAVIS}" ]; then
  source /code/bin/get-ssm-parameters.sh
  POSTGRES_NAME: $POSTGRES_NAME
  POSTGRES_HOST: $POSTGRES_HOST
  POSTGRES_PORT: $POSTGRES_PORT
fi

if [ "$POSTGRES_NAME" ]; then
  export PGPASSWORD=$POSTGRES_PASSWORD
  until psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -p "$POSTGRES_PORT" -d postgres -c '\q'
  do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 5
  done
fi

>&2 echo "Postgres is up"

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
