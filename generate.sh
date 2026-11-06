#!/bin/bash

cd ../meshlane
source .venv/bin/activate
git checkout typed
git status
git rev-parse --verify HEAD

stubgen src/meshlane --include-docstrings
rm -r ../meshlane-stubs/meshlane-stubs/*
mv out/meshlane/* ../meshlane-stubs/meshlane-stubs/
rm -d out/meshlane
rm -d out
