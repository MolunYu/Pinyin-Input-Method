# Pinyin-Input-Method
a simple pinyin input method implemented in python  
https://github.com/MolunYu/Pinyin-Input-Method

## Requirements
* python3
* sina_news_gbk: [download](https://cloud.tsinghua.edu.cn/smart-link/619913c2-c102-4d7c-a445-45df109e11e1/)

## Data Prepare
1. Download sina_news_gbk
2. Move sina_news_gbk to data/
```text
|-- Pinyin-Input-Method
    |-- data
        |-- sina_news_gbk
            |-- 2016-01.txt
            ...
            |-- 2016-09.txt
``` 
3. Data preprocessing 
```bash
cd ./src
python pre_process.py
```
4. Option: 3-gram and 4-gram required
```bash
cd ./src
python pre_gram3.py
python pre_gram4.py
```
5. Single_pinyin2word.json has a manual way to handle multi-tone words, 
if you don't need it, change with pinyin2word.json in viterbi_2gram.py, viterbi_gram3.py, viterbi_gram4.py
```python
# multi-tone word
with open("../data/single_pinyin2word.json", mode="r") as src:
    pinyin2word = json.load(src)
# normal
with open("../data/pinyin2word.json", mode="r") as src:
    pinyin2word = json.load(src)
```


## Usage
1. Transform pinyin to Chinese character
```bash
cd ./src
python pinyin.py --input=INPUT_FILE_PATH --output=OUTPUT_FILE_PATH
```
2. Transform pinyin in console interactively
```bash
cd ./src
python pinyin_interact.py
```
3. Test accuracy from given files.
Available test files in pinyin_test can be used as below. 
You can also use your files, make sure you have right format.
```bash
cd ./src
python acc.py --input=INPUT_FILE_PATH --ans=ANSWER_FILE_PATH
```
4. Change n-gram model in pinin.py, pinyin_interact.py, acc.py.
```python
# 2-gram
from viterbi_2gram import viterbi
# 3-gram
from viterbi_3gram import viterbi
# 4-gram
from viterbi_4gram import viterbi
```
## Baseline
1. 2-gram: ~86%
2. 3-gram: ~90%
3. 4-gram: ~91%


