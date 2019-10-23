from viterbi import viterbi


def count_same(s1, s2):
        return len([i for i in range(len(s1)) if s1[i] == s2[i]])


with open("../data/test_data.txt", mode="r", encoding="utf-8") as source:
    lines = [line.strip() for line in source.readlines()]
    test_pair = list(zip(lines[::2], lines[1::2]))

correct = sum([count_same(viterbi(pinyin.lower().split(" ")), sentence) for pinyin, sentence in test_pair])
total = sum([len(sentence) for _, sentence in test_pair])
print(correct / total)
