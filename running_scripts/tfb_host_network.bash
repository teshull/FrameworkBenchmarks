#!/bin/bash

cd $FRAMEWORK_DIR
SCRIPT_ROOT=$FRAMEWORK_DIR

test -t 1 && USE_TTY="-t"
docker build -t techempower/tfb - < ${SCRIPT_ROOT}/Dockerfile
exec docker run -i ${USE_TTY} --rm --network host -v /var/run/docker.sock:/var/run/docker.sock -v ${SCRIPT_ROOT}:/FrameworkBenchmarks techempower/tfb "${@}"
