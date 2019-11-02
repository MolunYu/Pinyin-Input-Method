from viterbi_3gram import viterbi_3gram
from multiprocessing import Pool


def count_same(s1, s2):
    count = 0
    s1 = viterbi_3gram(s1.strip().lower().split(" "))
    for i, j in zip(s1, s2.strip()):
        if i == j:
            count += 1
    if len(s1) - count > 3:
        print(s1.strip(), s2.strip())

    return count


if __name__ == '__main__':
    pool = Pool()
    with open("../data/pinyin_test/s_in.txt", mode="r", encoding="utf-8") as source:
        pinyin = source.readlines()

    with open("../data/pinyin_test/s_out.txt", mode="r", encoding="utf-8") as source:
        sentence = source.readlines()

    correct = pool.starmap(count_same, zip(pinyin, sentence))
    pool.close()
    pool.join()
    total = sum([len(i.strip()) for i in sentence])
    print(sum(correct) / total)
