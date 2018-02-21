# hiratsuka_crf_text
いま以下みたいのが出来ている
```
$ python3 test_crfmodel.py sentence_txt/matome_yen_ner.txt 0 money_model          2.3.0
[['日給', '名詞', '一般', '*', '*', '*', '*', '日給', 'ニッキュウ', 'ニッキュー', 'B-MNYUNIT'], ['9519円', '名詞', '固有名詞', '一般', '*', '*', '*', '9519円', 'キュウセンゴヒャクジュウキュウエン', 'キュウセンゴヒャクジュウキュウエン', 'B-MONEY'], ['以上', '名詞', '非自立', '副詞可能', '*', '*', '*', '以上', 'イジョウ', 'イジョー', 'I-MONEY'], ['を', '助詞', '格助詞', '一般', '*', '*', '*', 'を', 'ヲ', 'ヲ', 'B-OTHER'], ['希望', '名詞', 'サ変接続', '*', '*', '*', '*', '希望', 'キボウ', 'キボー', 'B-OTHER'], ['し', '動詞', '自立', '*', '*', 'サ変・スル', '連用形', 'する', 'シ', 'シ', 'B-OTHER'], ['ます', '助動詞', '*', '*', '*', '特殊・マス', '基本形', 'ます', 'マス', 'マス', 'B-OTHER']]
日給 9519円 以上 を 希望 し ます
Predicted: B-MNYUNIT B-MONEY I-MONEY B-OTHER B-OTHER B-OTHER B-OTHER
Correct:   B-MNYUNIT B-MONEY I-MONEY B-OTHER B-OTHER B-OTHER B-OTHER
```
