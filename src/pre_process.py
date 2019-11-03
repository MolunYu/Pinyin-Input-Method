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

    print("Program start :\nThe program will be completed in 7 minutes")
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
    word_freq = defaultdict(int)
    words_list = ((line[i] + line[i + 1] for i in range(len(line) - 1)) for line in pure_lines)

    for words in bar(words_list):
        for word in words:
            word_freq[word] += 1
    del words_list

    with open("../data/word2freq.json", mode="w") as target:
        json.dump(word_freq, target)
    del word_freq
    print("word prepared")

    # create dict {character : frequency}
    char2freq = Counter("".join(pure_lines))
    with open("../data/char2freq.json", mode="w") as target:
        json.dump(char2freq, target)
    print("char prepared")

    # create dict {pinyin : character}
    with open("../data/pinyin2word/pinyin2word.txt", mode="r", encoding="gbk") as source:
        pinyin2word = dict()

        # only trans 1st and 2nd word
        with open("../data/pinyin2word/1st_2nd_word.txt", mode="r", encoding="gbk ") as src:
            common_word = set(src.read())

        for line in source.readlines():
            line = line[:-1].split(" ")
            pinyin2word[line[0]] = [x for x in line[1:] if x in char2freq.keys() and x in common_word]

        with open("../data/pinyin2word.json", mode="w") as target:
            json.dump(pinyin2word, target)
    print("pinyin prepared")

    print("Time cost ", time.time() - start)
