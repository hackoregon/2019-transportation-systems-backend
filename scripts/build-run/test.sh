#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build, [-l] for a local PostGIS build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpl" opt; do
    case "$opt" in
        d)
          DEBUG=true
          sudo docker-compose run --name test-api --entrypoint /code/bin/test-entrypoint.sh   --rm 
          ;;
        p)
          DEBUG=false
          sudo docker-compose up
          ;;
        l)
          DEBUG=true
          sudo docker-compose -f local-postgis.yml run --name test-api \
            --entrypoint /code/bin/test-entrypoint.sh   --rm 
          ;;
        *)
          usage
          ;;
    esac
done

# fix ownership
echo "Fixing ownership on Linux"
if [ `uname -s` = "Linux" ]
then
  ls -l
  echo "sudo chown -R `id -u $USER`:`id -g $USER` ."
  sudo chown -R `id -u $USER`:`id -g $USER` .
  ls -l
fi
