#!/bin/sh

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo "SCRIPTPATH is $SCRIPTPATH"
cd $SCRIPTPATH
source env/bin/activate
FLASK_APP=observer.py python -m flask run
