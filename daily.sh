#!/usr/bin/env bash

cd /home/ylin/shareInfo
source ./env/bin/activate
python -u ./share/app/daliyUpdate.py 2>&1 >> log.log