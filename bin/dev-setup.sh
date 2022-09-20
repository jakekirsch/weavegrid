#! /bin/sh

# check for venv

# make venv
python -m venv venv
python -m pip install --upgrade pip
source venv/bin/activate
pip install -r requirements.txt
