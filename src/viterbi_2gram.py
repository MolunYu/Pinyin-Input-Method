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
        return char2freq[x2] * 1e-12


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

        for i in range(1, len(cells_2d)):
            cur_cells = cells_2d[i]
            pre_cells = cells_2d[i - 1]

            for cur in cur_cells:
                all_probs = [pre.prob * get_prob(pre.val, cur.val) for pre in pre_cells]
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
