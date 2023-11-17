#!/usr/bin/env bash
if [ -z "$1" ] ; then
    echo "Usage: ./run.sh <number>"
    exit 1
fi

make $1
./build/bin/$1/main
