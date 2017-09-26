# -*- coding: utf-8 -*-
import random
import pdb
import gc


def main():
    with open("tokens_81.txt", "r") as f:
        sentences = [sentence.replace("\n", "").split(" ") for sentence in f.readlines()]
    # 文脈の抽出
    context = []
    for sentence in sentences:
        sentence = [word for word in sentence if word != ""]
        for i in range(len(sentence)):
            rand = random.randint(1, 5)
            start = i - rand if i - rand >= 0 else 0
            end = i + rand + 1 if i + rand + 1 < len(sentence) else len(sentence)
            context.extend([sentence[i] + "\t" + sentence[j] for j in range(start, end) if i != j])
    text = list(set(context))

    # メモリ解放
    del sentence
    del sentences
    del context
    del rand
    gc.collect()

    with open("contexts.txt", "a") as f:
        for sentence in text:
            print(sentence)
            f.write(sentence)


if __name__ == "__main__":
    main()
