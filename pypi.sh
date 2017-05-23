# Adapted to LUCL use by G.A. Kaiping.
VENVS=~/venvs

cd $VENVS/pypi
. bin/activate
cd clldlucl
git pull origin master
git checkout tags/v$1
python setup.py sdist register upload

