from viterbi import viterbi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
args = parser.parse_args()

with open(args.filename, mode="r") as source:
    for line in source.readlines():
        print(viterbi(line[:-1].split(" ")))


