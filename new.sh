#!/usr/bin/env bash
if [ -z "$1" ] ; then
    echo "Usage: ./new.sh <number> <type>"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "Usage: ./new.sh <number> <type>"
    exit 1
fi

if [ "$2" = "python" ] ; then
    mkdir -p src/$1
    exec 3>src/$1/main.py
    echo -n $'#\n# Leetcode Problem ' >&3
    echo -n $1 >&3
    echo $':\n# Solution by James Errington, 2024\n#\n\nclass Solution:' >&3
else
    mkdir -p src/$1
    exec 3>src/$1/main.cpp
    echo -n $'/*\n * Leetcode Problem ' >&3
    echo -n $1 >&3
    echo $':\n * Solution by James Errington, 2024\n*/\n\n#include "../shared.hpp"\n\nclass Solution {\npublic:\n\n};\n\nint main() {\n\n};' >&3
fi
