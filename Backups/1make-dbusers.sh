#! /bin/bash

# create the user we'll be restoring to!
if [ "${DJANGO_POSTGRES_USER}" = "postgres" ]
then
  echo "'postgres' already exists - exiting normally"
else
  echo "Creating database user '${DJANGO_POSTGRES_USER}'"
  createuser --superuser ${DJANGO_POSTGRES_USER}
  command="ALTER USER \"${DJANGO_POSTGRES_USER}\" WITH PASSWORD '${DJANGO_POSTGRES_PASSWORD}';"
  psql -c "$command"
fi
echo "User creation completed"
