#!/usr/bin/env bash
if [ -z "$1" ] ; then
    echo "Usage: ./run.sh <number>"
    exit 1
fi

mkdir -p src/$1
exec 3>src/$1/main.cpp
echo -n $'/*\n * Leetcode Problem ' >&3
echo -n $1 >&3
echo $':\n * Solution by James Errington, 2023\n*/\n\n#include "../shared.hpp"\n\nclass Solution {\npublic:\n\n};\n\nint main() {\n\n};' >&3
