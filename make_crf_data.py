# -*- coding: utf-8 -*-

import MeCab
import os
import glob
import sys

args = sys.argv

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab.parse('')

def makePreCrfData(mecab,sentence):

    node = mecab.parse(sentence)

    arySentence = []
    for chunk in node.splitlines()[:-1]:
        nodeParts = []
        (surface, feature) = chunk.split('\t')
        nodeParts.append(surface)
        aryFeature = feature.split(',')
        mergeList = nodeParts+aryFeature
        arySentence.append(mergeList)

    arySentence.append([])
    return arySentence

# ディレクトリのファイル一覧を取得
filelist = glob.glob('sentence_txt/*')
for strfile in filelist:

    # ファイル名を分割
    aryFile = strfile.split(".")

    # 書き込み用のファイル名を定義
    strWriteFile = aryFile[0]+"_feature.txt"

    # 形態素解析して、それをファイルに書き込み
    with open(strfile,'r') as f:

        aryAllSentenceFeature = []

        lines = f.readlines()

        for line in lines:
            if line != None:
                arySentenceFeature = makePreCrfData(mecab,line)
                aryAllSentenceFeature = aryAllSentenceFeature+arySentenceFeature

        with open(strWriteFile,'w') as fw:
            aryFeature = []
            for arySentenceFeature in aryAllSentenceFeature:
                strLine = "\t".join(arySentenceFeature)
                aryFeature.append(strLine)
            
            fw.write('\n'.join(aryFeature))
