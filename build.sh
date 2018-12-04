#!/usr/bin/env bash

python setup.py sdist

VENVS=~/venvs
WORKING=`pwd`

cd $VENVS
python3 -m venv testapp
cd testapp
. bin/activate
pip install -U setuptools
pip install -U pip
pip install "$WORKING/dist/clldlucl-$1.tar.gz"
pcreate -t clldlucl_app testapp
cd testapp
pip install -e .[test]
python testapp/scripts/initializedb.py development.ini
pytest
cd $VENVS
rm -rf testapp
