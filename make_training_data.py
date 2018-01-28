# -*- coding: utf-8 -*-
#
# trainningデータの作成
#
import os

jobList = []
jobSentenceList = []
locationList = []
locationSentenceList = []
monthList = []
monthSentenceList = []
dayList = []
daySentenceList = []
yearList = []
yearSentenceList = []
monthDaySentenceList = []

with open('job_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        jobList.append(strLine)

with open('job.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # JOBを置換
        for job in jobList:
            strText = strLine.replace('JOB',job)
            jobSentenceList.append(strText)

    # ファイルに書き込む
    with open('job_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(jobSentenceList))


#-------------------------------------------------------------------
# 位置
with open('location_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        locationList.append(strLine)


with open('location.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # JOBを置換
        for location in locationList:
            strText = strLine.replace('LOCATION',location)
            locationSentenceList.append(strText)

    
    # ファイルに書き込む
    with open('location_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(locationSentenceList))

#-------------------------------------------------------------------
# 日 
with open('day_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        dayList.append(strLine)


with open('day.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # DAYを置換
        for day in dayList:
            strText = strLine.replace('DAY',day)
            daySentenceList.append(strText)

    
    # ファイルに書き込む
    with open('day_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(daySentenceList))


#-------------------------------------------------------------------
# 月 
with open('month_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        monthList.append(strLine)


with open('month.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # DAYを置換
        for month in monthList:
            strText = strLine.replace('MONTH',month)
            monthSentenceList.append(strText)

    
    # ファイルに書き込む
    with open('month_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(monthSentenceList))

#-------------------------------------------------------------------
# 年 
with open('year_list.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()
        yearList.append(strLine)


with open('year.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # YEARを置換
        for year in yearList:
            strText = strLine.replace('YEAR',year)
            yearSentenceList.append(strText)

    
    # ファイルに書き込む
    with open('year_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(yearSentenceList))

#-------------------------------------------------------------------
# 月、日 
with open('day_month.txt', 'r') as f:
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    for line in lines:
        strLine = line.strip()

        # MONTHを置換
        for month in monthList:
            strText = strLine.replace('MONTH',month)
            
            for day in dayList:
                strDayMonth = strText.replace('DAY',day)
                monthDaySentenceList.append(strDayMonth)
    
    # ファイルに書き込む
    with open('day_month_sentence.txt', 'w') as fw:
        # 書き込み
        fw.write('\n'.join(monthDaySentenceList))

