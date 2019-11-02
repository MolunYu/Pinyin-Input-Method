from viterbi_3gram import viterbi_3gram
from tqdm import tqdm


def count_same(s1, s2):
    count = 0
    s1 = viterbi_3gram(s1.strip().lower().split(" "))
    for i, j in zip(s1, s2.strip()):
        if i == j:
            count += 1

    return count


def get_acc(src, dst):
    with open("../data/pinyin_test/{}".format(src), mode="r", encoding="utf-8") as source:
        pinyin = source.readlines()

    with open("../data/pinyin_test/{}".format(dst), mode="r", encoding="utf-8") as source:
        sentence = source.readlines()

    correct = 0
    for i, j in tqdm(zip(pinyin, sentence)):
        correct += count_same(i, j)

    total = sum([len(i.strip()) for i in sentence])
    print(correct / total)

get_acc("s_in.txt", "s_out.txt")
get_acc("news_input.txt", "news_output.txt")
get_acc("input.txt", "output.txt")