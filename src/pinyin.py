from viterbi import viterbi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, required=True, help="input file path")
parser.add_argument("--output", type=str, help="output file path")
args = parser.parse_args()

with open(args.input, mode="r") as source:
    result = list()
    for line in source.readlines():
        sentence = viterbi(line[:-1].split(" "))
        print(sentence)
        result.append(sentence + "\n")

    if args.output:
        with open("output.txt", mode="w") as target:
            target.writelines(result)





