import json
import re
from collections import Counter
import time


def get_news(line):
    # \u4e00-\u9fa5 为中文Unicode编码范围
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    # 多数新闻以"原标题"开头，影响频率计算
    news = json.loads(line.strip())["html"].replace("原标题", "")
    return re.sub(pattern, "", news)


# start = time.time()
# print("Program start :\nThis Program may finish in 5 minutes")
# paths = ["../data/sina_news_gbk/2016-0{}.txt".format(num) for num in range(1, 10)]
#
# # create only character form
# lines = list()
# for path in paths:
#     with open(path, mode="r", encoding="gbk") as source:
#         lines.extend(source.readlines())
#
# data = "".join([get_news(line) for line in lines])
# print("data prepared")
#
# # create dict {character : frequency}
# char2freq = Counter(data)
# word_freq = Counter((i + j for (i, j) in zip(data[:-1], data[1:])))
#
# with open("../data/char2freq.json", mode="w") as target:
#     json.dump(char2freq, target)
#
# with open("../data/word2freq.json", mode="w") as target:
#     json.dump(word_freq, target)
# print("freq prepared")

# create dict {pinyin : character}
with open("../data/pinyin2word/pinyin2word.txt", mode="r") as source:
    pinyin2word = dict()

    # only trans 1st and 2nd word
    with open("../data/pinyin2word/1st_2nd_word.txt", mode="r") as src:
        common_word = set(src.read())

    with open("../data/char2freq.json", mode="r") as src:
        char2freq = json.load(src)

    for line in source.readlines():
        line = line[:-1].split(" ")
        pinyin2word[line[0]] = [x for x in line[1:] if x in char2freq.keys() and x in common_word]

    with open("../data/pinyin2word.json", mode="w") as target:
        json.dump(pinyin2word, target)
print("pinyin prepared")

# print("Time cost ", time.time() - start)
