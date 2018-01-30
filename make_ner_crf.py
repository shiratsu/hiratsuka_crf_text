# -*- coding: utf-8 -*-
#
# 形態素解析が終わってるファイルに
# 固有表現抽出を追加していく

import re
import glob

# ディレクトリのファイル一覧を取得
filelist = glob.glob('sentence_txt/*feature.txt')

aryUpdateFeature = []

for strfile in filelist:

    # ファイル名を分割
    aryFile = strfile.split(".")

    # 書き込み用のファイル名を定義
    strWriteFile = aryFile[0]+"_ner.txt"
    
    # ファイルを開く
    with open(strFile,'r') as f:

        lines = f.readlines()

        for line in lines:
            aryLine = line.split("\t")

            if strfile.find('date'):
                aryLine.append('B-DATE')
            elif strfile.find('day') or strfile.find('month') or strfile.find('year'):
                aryLine.append('B-DATE')
            elif strfile.find('location'):
                aryLine.append('B-LOC')
            
            aryUpdateFeature.append("\t".join(aryLine))

        with open(strWriteFile,'w') as fw:
            fw.write('\n'.join(aryUpdateFeature))
