# -*- coding: utf-8 -*-
#
# 訓練されたもののテストを実行する
#

from itertools import chain
import pycrfsuite
import sklearn
import make_crf_model 
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer

import sys
import codecs


if __name__ == '__main__':

    args = sys.argv
    
    c = make_crf_model.CorpusReader(args[1])
    train_sents = c.iob_sents('train')
    test_sents = c.iob_sents('test')

    tagger = pycrfsuite.Tagger()
    tagger.open(args[3]+'.crfsuite')

    example_sent = test_sents[0]
    if len(args) == 4:
        example_sent = test_sents[int(args[2])]

    print(example_sent)
    print("-------------------------")
    print(' '.join(make_crf_model.sent2tokens(example_sent)))
    print("-------------------------")
    print(make_crf_model.sent2features(example_sent))
    print("-------------------------")
    print("-------------------------")

    print("Predicted:", ' '.join(tagger.tag(make_crf_model.sent2features(example_sent))))
    print("Correct:  ", ' '.join(make_crf_model.sent2labels(example_sent)))
