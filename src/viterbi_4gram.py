import json
import sys


class ViterbiCell:
    def __init__(self, val, sequence=""):
        self.val = val
        self.prob = char2freq[val]
        self.sequence = sequence


def get_prob(x1, x2):
    if x1 + x2 in word2freq:
        return word2freq[x1 + x2] / char2freq[x1]
    else:
        return char2freq[x2] * 1e-10


def get_prob_3gram(x12, x3):
    x1, x2 = x12
    if x12 + x3 in three2freq and x12 in word2freq:
        return three2freq[x12 + x3] / word2freq[x12]
    else:
        return get_prob(x2, x3)


def get_prob_4gram(x123, x4):
    x1, x2, x3 = x123
    if x123 + x4 in four2freq and x123 in three2freq:
        return four2freq[x123 + x4] / three2freq[x123]
    else:
        return get_prob_3gram(x2 + x3, x4)


def viterbi(sentence):
    try:
        cells_2d = [[ViterbiCell(v) for v in pinyin2word[x]] for x in sentence]
    except KeyError:
        return "PinyinError: check pinyin and space: {}".format(sentence)
    else:
        if len(sentence) == 1:
            return sorted(pinyin2word[sentence[0]], key=lambda x: char2freq[x])[-1]

        for cell in cells_2d[0]:
            cell.sequence = cell.val

        if len(cells_2d) > 1:
            for cur in cells_2d[1]:
                all_probs = [pre.prob * get_prob(pre.val, cur.val) for pre in cells_2d[0]]
                pre_index, cur.prob = sorted(enumerate(all_probs), key=lambda x: x[1])[-1]
                cur.sequence = cells_2d[0][pre_index].sequence + cur.val

        if len(cells_2d) > 2:
            for cur in cells_2d[2]:
                all_probs = [pre.prob * get_prob_3gram(pre.sequence[-2:], cur.val) for pre in cells_2d[1]]
                pre_index, cur.prob = sorted(enumerate(all_probs), key=lambda x: x[1])[-1]
                cur.sequence = cells_2d[1][pre_index].sequence + cur.val

        for i in range(3, len(cells_2d)):
            cur_cells = cells_2d[i]
            pre_cells = cells_2d[i - 1]

            for cur in cur_cells:
                all_probs = [pre.prob * get_prob_4gram(pre.sequence[-3:], cur.val) for pre in pre_cells]
                pre_index, cur.prob = sorted(enumerate(all_probs), key=lambda x: x[1])[-1]
                cur.sequence = pre_cells[pre_index].sequence + cur.val
                # print("{}: {}".format(cur.sequence, cur.prob))

        return sorted(cells_2d[-1], key=lambda x: x.prob)[-1].sequence


print("Model loading ...")
print("load pinyin2word ...")
with open("../data/single_pinyin2word.json", mode="r") as source:
    pinyin2word = json.load(source)

print("load char2freq ...")
with open("../data/char2freq.json", mode="r") as source:
    char2freq = json.load(source)

print("load word2freq ...")
sys.stdout.flush()
with open("../data/word2freq.json", mode="r") as source:
    word2freq = json.load(source)

print("load three2freq ...")
sys.stdout.flush()
with open("../data/three2freq.json", mode="r") as src:
    three2freq = json.load(src)

print("load four2freq ...")
sys.stdout.flush()
with open("../data/four2freq.json", mode="r") as src:
    four2freq = json.load(src)
