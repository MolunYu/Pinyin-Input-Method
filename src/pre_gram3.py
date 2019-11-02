import json
import re
from collections import Counter, defaultdict
import time
from tqdm import tqdm


def get_news(lines):
    pure_lines = list()
    p = ',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|：' \
        '|‘|\'|【|】|·|！| |…|（|）|[a-z]|[A-Z]|[0-9]'

    for line in tqdm(lines):
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

    print("Program start :\nThe program will be completed in 8 minutes")
    paths = ["../data/sina_news_gbk/2016-0{}.txt".format(num) for num in range(1, 10)]

    # get pure lines
    lines = list()
    for path in tqdm(paths):
        with open(path, mode="r", encoding="gbk") as source:
            lines.extend(source.readlines())

    pure_lines = get_news(lines)
    del lines
    print("data prepared")

    # create dict {word : frequency}
    word3_freq = defaultdict(int)
    words3_list = ((line[i] + line[i + 1] + line[i + 2] for i in range(len(line) - 2)) for line in pure_lines)

    for words in tqdm(words3_list):
        for word in words:
            word3_freq[word] += 1
    del words3_list

    with open("../data/three2freq.json", mode="w") as target:
        json.dump(word3_freq, target)
    del word3_freq
    print("word3 prepared")

    print("Time cost ", time.time() - start)
