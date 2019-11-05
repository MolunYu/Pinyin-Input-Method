from viterbi_3gram import viterbi
from bar import bar
import argparse


def count_same(s1, s2):
    count = 0
    s1 = viterbi(s1.strip().lower().split(" "))
    for i, j in zip(s1, s2.strip()):
        if i == j:
            count += 1

    return count


def get_acc(src, dst):
    with open(src, mode="r", encoding="utf-8") as source:
        pinyin = source.readlines()

    with open(dst, mode="r", encoding="utf-8") as source:
        sentence = source.readlines()

    correct = 0
    for i, j in bar(zip(pinyin, sentence)):
        correct += count_same(i, j)

    total = sum([len(i.strip()) for i in sentence])
    return correct / total

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="input file path")
    parser.add_argument("--ans", type=str, help="answer file path")
    args = parser.parse_args()

    print(get_acc(args.input, args.ans))
