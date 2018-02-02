# -*- coding: utf-8 -*-
#
# 形態素解析が終わってるファイルに
# 固有表現抽出を追加していく

import re
import glob

# ディレクトリのファイル一覧を取得
filelist = glob.glob('sentence_txt/*feature.txt')


for strfile in filelist:

    # 分類をした後に入れる箱を定義
    aryUpdateFeature = []

    # ファイル名を分割
    aryFile = strfile.split(".")

    # 書き込み用のファイル名を定義
    strWriteFile = aryFile[0]+"_ner.txt"
    
    print(strfile)
    
    # ファイルを開く
    with open(strfile,'r') as f:

        lines = f.readlines()

        for line in lines:
            aryLine = line.split("\t")

            strWord = aryLine[0]

            if strfile.find('date') != -1:
                #print(strWord)
                aryLine.append('B-DATE')
            
            elif strfile.find('day') != -1 or strfile.find('month') != -1 or strfile.find('year') != -1:
                
                #print(strWord)
                if strWord not in ['がつ','/','に','ち']:
                    aryLine.append('B-DATE')
                else:
                    print("--------------------------")
                    print("I-DATE")
                    print(strWord)
                    aryLine.append('I-DATE')

            elif strfile.find('location') != -1:
                aryLine.append('B-LOC')
            
            elif strfile.find('job') != -1:
                aryLine.append('B-JOB')
            
            aryUpdateFeature.append("\t".join(aryLine))

        with open(strWriteFile,'w') as fw:
            fw.write('\n'.join(aryUpdateFeature))
