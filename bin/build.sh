#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build, [-l] for a local PostGIS build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpl" opt; do
    case "$opt" in
        d)
          DEBUG=true
          sudo docker-compose build --build-arg DEBUG=true
          ;;
        p)
          DEBUG=false
          sudo docker-compose build --build-arg DEBUG=false
          ;;
        l)
          DEBUG=true
          sudo docker-compose -f local-postgis.yml build --build-arg DEBUG=true
          ;;
        *)
          usage
          ;;
    esac
done
