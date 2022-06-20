#!/bin/sh

set -e

pip install -r requirements.txt

#cd app
#alembic upgrade head
#cd ../..

python -m app.app
