#!/bin/bash

# Use python3 and pip3
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
