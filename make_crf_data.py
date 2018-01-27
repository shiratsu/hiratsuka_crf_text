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

    print(arySentence)    
