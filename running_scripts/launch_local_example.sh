#!/bin/bash


./launch_local.sh \
    --mode benchmark \
    --test play2-scala \
    --type plaintext \
    --pipeline-concurrency-levels 4096 \
    --duration 60 \
    --kamon-args testparam=fakevalue
