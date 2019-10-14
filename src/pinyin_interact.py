from viterbi import viterbi

print("This a program tranform pinyin sequence into sentence\n"
      "Enter pinyin sequence to continue or 'exit' to exit\n"
      "Make sure pinyin sequence is separated by space correctly\n")

sentence = input("Input sequence: ")
while sentence != "exit":
    print("output: " + viterbi(sentence.strip().split(" ")), end="\n\n")
    sentence = input("Input: ")

