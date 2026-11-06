#!/bin/bash

set -e

source .venv/bin/activate

cd ../meshlane
git checkout typed
git status
git rev-parse --verify HEAD

cd -

rm -rf meshlane-stubs meshlane
stubgen --no-import ../meshlane/src/meshlane --include-docstrings -o .
mv meshlane meshlane-stubs
