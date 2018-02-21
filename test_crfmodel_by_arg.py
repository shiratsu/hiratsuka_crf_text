# -*- coding: utf-8 -*-
#
# 訓練されたもののテストを実行する
#
import pycrfsuite
import sys
import MeCab
import re
import make_crf_model
args = sys.argv

#上で学習しやすいようにstr型を学習しやすい形に変える。見辛過ぎますね。すみません。
def text2sent(text):
    sent =[]
    m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokens = [re.split("[\t,]",line) for line in m.parse(text).split('\n')]
    print(tokens)
    #print(text)
    for i in range(len(tokens)-2):
        token = tokens[i][0]
        p1 = "*"
        p2 = "*"
        p3 = "*"
        p4 = "*"
        f1='*'
        f2='*'
        #print("--------------")        
        #print(len(tokens[i]))        
        #print(token)        
        #print(tokens[i])        
        #print("--------------")        
        if len(tokens[i])<=3:
            p1 = "*"
            p2 = "*"
            p3 = "*"
            p4 = "*"
        else:
            part = tokens[i][3].split('-')
            p1 = part[0]
            if len(part) == 2:
                p2 = part[1]
                p3 = "*"
                p4 = "*"
            if len(part) == 3:
                p2 = part[1]
                p3 = part[2]
                p4 = "*"
            elif len(part) == 4:
                p2 = part[1]
                p3 = part[2]
                p4 = part[3]
            else:
                p2 = "*"
                p3 = "*"
                p4 = "*"
            form = [tokens[i][4],tokens[i][5]]
            if form[0]=='':
                f1='*'
                f2='*'
            else:
                f1 = form[0]
                f2 = form[1]
        if len(tokens[i]) > 1:        
            sent.append([token,p1,p2,p3,p4,f1,f2,tokens[i][2],tokens[i][1],tokens[i][1]])
            #sent.append([token,p1,p2,p3,p4,f1,f2,'*',tokens[i][1],tokens[i][1]])
        print(sent)
    return sent

#上で学習したモデルをロード
tagger = pycrfsuite.Tagger()
tagger.open(args[1]+'.crfsuite')

#適当にtextを綺麗にする。
text = args[2]   #好きなテキストを入れよう
text = text.replace("\u3000","。")
text = re.sub('[^(a-zA-Z0-9ぁ-んァ-ン一-龥 。ー)]',"",text)
text = text.replace('br','。')

#textをsent（上で学習するための型?）へ変換する。
sent = text2sent(text)

#tokenと予測したTagをつけたものをlistで保存
tokenlist = make_crf_model.sent2tokens(sent)
predictlist = tagger.tag(make_crf_model.sent2features(sent))

print(sent)
print("--------------")
print(tokenlist)
print("--------------")
print(make_crf_model.sent2features(sent))
print("--------------")
print(predictlist)


#表示
#wordlist = []
#for i in range(len(tokenlist)):
#    if predictlist[i][0] == "B":
#        wordlist.append((tag,word))
#        word = tokenlist[i]
#        tag = predictlist[i][-3:]
#    if predictlist[i][0] == "I":
#        word+=tokenlist[i]
#    if predictlist[i][0] == "O":
#        pass
#set(wordlist.sort())
