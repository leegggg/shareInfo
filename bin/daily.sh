#!/usr/bin/env bash

cd /home/ylin/shareInfo
source ./env/bin/activate
python -u ./share/app/daliyUpdate.py >> log.log 2>&1