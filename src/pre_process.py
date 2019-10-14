import json
import re
from collections import Counter

paths = ["../data/sina_news_gbk/2016-0{}.txt".format(num) for num in range(1, 10)]

# create only character form
with open("../data/dataset.txt", mode="w") as target:
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    for path in paths:
        with open(path, mode="r") as source:
            for line in source.readlines():
                data = str(dict(json.loads(line, "gbk"))["html"]).replace("原标题", "")
                character = re.sub(pattern, "", data)
                target.write(character)

# create dict {character : frequency}
with open("../data/dataset.txt", mode="r") as source:
    data = source.read()
    char2freq = Counter(data)
    with open("../data/char2freq.json", mode="w") as target:
        json.dump(char2freq, target)

# create dict {word : frequency}
with open("../data/dataset.txt", mode="r") as source:
    data = source.read()
    word_freq = Counter((i + j for (i, j) in zip(data[:-1], data[1:])))
    with open("../data/word2freq.json", mode="w") as target:
        json.dump(word_freq, target)

# create dict {pinyin : character}
with open("../data/pinyin2word/pinyin2word.txt", mode="r") as source:
    pinyin2word = dict()

    for line in source.readlines():
        line = line[:-1].split(" ")
        pinyin2word[line[0]] = [x for x in line[1:] if x in char2freq.keys()]

    with open("../data/pinyin2word.json", mode="w") as target:
        json.dump(pinyin2word, target)