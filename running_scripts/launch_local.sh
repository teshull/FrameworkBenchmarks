#!/bin/bash


${FRAMEWORK_DIR}/running_scripts/tfb_host_network.bash \
    --server-host 127.0.0.1 \
    --database-host 127.0.0.1 \
    --client-host 127.0.0.1 \
    --network-mode host \
    "$@"
