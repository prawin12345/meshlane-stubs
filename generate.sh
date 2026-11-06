#!/bin/bash

set -e

source .venv/bin/activate

cd ../meshlane
git checkout typed
git status
git rev-parse --verify HEAD

cd -

rm -r meshlane-stubs
stubgen -p meshlane --search-path ../meshlane/src --include-docstrings -o .
mv meshlane meshlane-stubs
