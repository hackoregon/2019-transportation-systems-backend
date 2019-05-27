#! /bin/bash

if [ `( ls -1 /Backups/*.backup 2>/dev/null || true ) | wc -l` -gt "0" ]
then
  for file in /Backups/*.backup
  do
    echo "Creating database '${DJANGO_POSTGRES_NAME}' with owner '${DJANGO_POSTGRES_USER}'"
    createdb --owner=${DJANGO_POSTGRES_USER} ${DJANGO_POSTGRES_NAME}
    echo "Creating 'postgis' extension in ${DJANGO_POSTGRES_USER}"
    psql --username=${DJANGO_POSTGRES_USER} --dbname=${DJANGO_POSTGRES_NAME} \
      --command="CREATE EXTENSION IF NOT EXISTS postgis CASCADE;"
    echo "Restoring $file"
    pg_restore --dbname=${DJANGO_POSTGRES_NAME} $file
    echo "Restore completed"
  done
fi

if [ `( ls -1 /Backups/*.sql.gz 2>/dev/null || true ) | wc -l` -gt "0" ]
then
  for file in /Backups/*.sql.gz
  do
    echo "Restoring $file"
    gzip -dc $file | psql
    echo "Restore completed"
  done
fi

if [ `( ls -1 /Backups/*.sql 2>/dev/null || true ) | wc -l` -gt "0" ]
then
  for file in /Backups/*.sql
  do
    echo "Restoring $file"
    psql < $file
    echo "Restore completed"
  done
fi
