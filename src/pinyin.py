from viterbi_3gram import viterbi
import argparse
from bar import bar

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, required=True, help="input file path")
parser.add_argument("--output", type=str, required=True, help="output file path")
args = parser.parse_args()

with open(args.input, mode="r") as source:
    result = list()
    for line in bar(source.readlines()):
        sentence = viterbi(line.strip().split(" "))
        result.append(sentence + "\n")

    with open(args.output, mode="w", encoding="utf-8") as target:
        target.writelines(result)
