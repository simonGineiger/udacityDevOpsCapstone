#!/bin/bash
python3 -m venv ~/.udacity-devops
source ~/.udacity-devops/bin/activate
pip install --upgrade pip &&\
  pip install -r requirements.txt
pylint --disable=C *.py

