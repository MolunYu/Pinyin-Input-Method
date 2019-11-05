# Pinyin-Input-Method
a simple pinyin input method implemented in python  
https://github.com/MolunYu/Pinyin-Input-Method

## Requirements
* python3
* sina_news_gbk: [download](https://cloud.tsinghua.edu.cn/smart-link/619913c2-c102-4d7c-a445-45df109e11e1/)

## Directory
```text
Pinyin-Input-Method
│  README.md
│  
├─data
│  │  acc_result.yaml
│  │  char2freq.json    //一元词频
│  │  four2freq.json    //四元词篇    
│  │  pinyin2word.json  //拼音转汉字
│  │  single_pinyin2word.json   //拼音转汉字(多音字处理版)
│  │  three2freq.json   //三元词频
│  │  word2freq.json    //二元词篇
│  │  
│  ├─pinyin2word
│  │      1st_2nd_word.txt
│  │      input.txt
│  │      multi_10000word.txt
│  │      multi_word.xlsx
│  │      output.txt
│  │      pinyin2word.txt
│  │      README.txt
│  │      
│  ├─pinyin_test    //测试文件目录(in-ans为一对测试数据)
│  │      common_ans.txt
│  │      common_in.txt
│  │      mini_ans.txt
│  │      mini_in.txt
│  │      news_ans.txt
│  │      news_in.txt
│  │      
│  └─sina_news_gbk
│          下载地址.txt
│          
└─src
      |  acc.py //准确率测试
      |  bar.py 
      |  pinyin.py  //转换拼音文件为句子
      |  pinyin_interact.py //交互式转换拼音文件
      |  pre_gram3.py   //3-gram 预处理
      |  pre_gram4.py   //4-gram 预处理
      |  pre_process.py //2-gram 预处理(3-gram,4-gram前执行)
      |  viterbi_2gram.py   //2-gram 译码
      |  viterbi_3gram.py   //3-gram 译码
      |  viterbi_4gram.py   //4-gram 译码
        

```

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


