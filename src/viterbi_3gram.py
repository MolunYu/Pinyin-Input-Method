import json


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


def viterbi_3gram(sentence):
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

        for i in range(2, len(cells_2d)):
            cur_cells = cells_2d[i]
            pre_cells = cells_2d[i - 1]

            for cur in cur_cells:
                all_probs = [pre.prob * get_prob_3gram(pre.sequence[-2:], cur.val) for pre in pre_cells]
                pre_index, cur.prob = sorted(enumerate(all_probs), key=lambda x: x[1])[-1]
                cur.sequence = pre_cells[pre_index].sequence + cur.val
                # print("{}: {}".format(cur.sequence, cur.prob))

        return sorted(cells_2d[-1], key=lambda x: x.prob)[-1].sequence


with open("../data/single_pinyin2word.json", mode="r") as src:
    pinyin2word = json.load(src)

with open("../data/char2freq.json", mode="r") as src:
    char2freq = json.load(src)

with open("../data/word2freq.json", mode="r") as src:
    word2freq = json.load(src)

with open("../data/three2freq.json", mode="r") as src:
    three2freq = json.load(src)
