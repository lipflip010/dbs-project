#!/bin/bash
python3 -m venv ./env
cd env/bin
source activate
pip3 install -r ../../requirements.txt