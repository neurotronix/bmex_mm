#!/usr/bin/env bash

MM="python ./marketmaker"

until $MM; do
    echo "$MM crashed with exit code $?. Restarting ..." >&2
done
