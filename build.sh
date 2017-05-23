#!/bin/sh

# Adapted to LUCL use by G.A. Kaiping.

VENVS=~/venvs

cd $VENVS/cheesecake
. bin/activate
cd clldlucl
git checkout master
git pull origin master
python setup.py sdist
cheesecake_index --path="dist/clldlucl-$1.tar.gz" --with-pep8

cd $VENVS
virtualenv testapp
cd testapp
. bin/activate
pip install "$VENVS/cheesecake/clldlucl/dist/clldlucl-$1.tar.gz"
pcreate -t clldlucl_app testapp
cd testapp
python setup.py develop
python testapp/scripts/initializedb.py development.ini
pip install nose
pip install mock==1.0
nosetests
cd $VENVS
rm -rf testapp

