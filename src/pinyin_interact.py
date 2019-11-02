from viterbi_3gram import viterbi_3gram

print("This a program tranform pinyin sequence into sentence!\n"
      "Enter pinyin sequence to continue or 'exit' to exit.\n"
      "Make sure pinyin sequence is separated by space correctly!\n")

sentence = input("In: ")
while sentence != "exit":
    print("Out: " + viterbi_3gram(sentence.lower().strip().split(" ")), end="\n\n")
    sentence = input("In: ")

