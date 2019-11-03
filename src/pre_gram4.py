import json
import re
from collections import Counter, defaultdict
import time
from bar import bar


def get_news(lines):
    pure_lines = list()
    p = ',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|：' \
        '|‘|\'|【|】|·|！| |…|（|）|[a-z]|[A-Z]|[0-9]'

    for line in bar(lines):
        news = json.loads(line.strip())
        title = news['title']
        text = news['html']

        for i in re.split(p, title):
            if i:
                pure_lines.append(i)

        for i in re.split(p, text):
            if i:
                pure_lines.append(i)

    return pure_lines


if __name__ == '__main__':
    start = time.time()

    print("Program start :\nThe program will be completed in 11 minutes")
    paths = ["../data/sina_news_gbk/2016-0{}.txt".format(num) for num in range(1, 10)]

    # get pure lines
    lines = list()
    for path in bar(paths):
        with open(path, mode="r", encoding="gbk") as source:
            lines.extend(source.readlines())

    pure_lines = get_news(lines)
    del lines
    print("data prepared")

    # create dict {word : frequency}
    word4_freq = defaultdict(int)
    words4_list = ((line[i] + line[i + 1] + line[i + 2] + line[i + 3] for i in range(len(line) - 3))
                    for line in pure_lines)

    for words in bar(words4_list):
        for word in words:
            word4_freq[word] += 1
    del words4_list

    compress_four2freq = dict()
    for key, val in bar(word4_freq.items()):
        if int(val) > 1:
            compress_four2freq[key] = val
    del word4_freq

    with open("../data/four2freq.json", mode="w") as target:
        json.dump(compress_four2freq, target)
    print("word4 prepared")

    print("Time cost ", time.time() - start)
