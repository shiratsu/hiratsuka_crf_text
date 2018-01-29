# -*- coding: utf-8 -*-

import MeCab

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

    return arySentence


# 形態素解析して、それをファイルに書き込み
with open('all_sentence.txt','r') as f:

    aryAllSentenceFeature = []

    lines = f.readlines()

    for line in lines:
        if line != None:
            arySentenceFeature = makePreCrfData(mecab,line)
            aryAllSentenceFeature = aryAllSentenceFeature+arySentenceFeature
    print(aryAllSentenceFeature)

    with open('all_sentence_feature.txt','w') as f:
        aryFeature = []
        for arySentenceFeature in aryAllSentenceFeature:
            strLine = "\t".join(arySentenceFeature)
            aryFeature.append(strLine)
        
        fw.write('\n'.join(aryFeature))
