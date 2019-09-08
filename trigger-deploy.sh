#! /bin/bash

bumpversion $1 --config-file ./hackoregon_transportation_systems/setup.cfg  && git push && git push --tags