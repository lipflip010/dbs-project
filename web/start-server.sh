#!/bin/bash
source ./env/bin/activate
cd src
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run

