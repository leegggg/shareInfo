#!/usr/bin/env bash

cd /home/ylin/shareInfo
source ../env/bin/activate
logfile=all.log


python -u ./share/app/daliyUpdate.py >> ${logfile} 2>&1

python -u ./share/app/updateBasicInfo.py   >> ${logfile} 2>&1
python -u ./share/app/updateMacro.py   >> ${logfile} 2>&1

python -u ./share/app/updateReference.py >>${logfile} 2>&1
python -u ./share/app/updateReference.py   >> ${logfile} 2>&1
python -u ./share/app/updateReports.py  >> ${logfile} 2>&1
python -u ./share/app/updateBoxoffice.py   >> ${logfile} 2>&1


python -u ./share/app/getAllDayLines.py   >> ${logfile} 2>&1