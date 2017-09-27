# -*- coding: utf-8 -*-
import random
import pdb
import gc


def main():
    sentences = []
    with open("tokens_81.txt", "r") as rf:
        for sentence in rf.readlines():
            context = []
            words = [word for word in sentence.replace("\n", " ").split(" ") if word != ""]
            if len(words) < 2:
                continue
            # 文脈の抽出
            for i in range(len(words)):
                rand = random.randint(1, 5)
                start = i - rand if i - rand >= 0 else 0
                end = i + rand + 1 if i + rand + 1 < len(words) else len(words)
                context.extend([words[i] + "\t" + words[j] for j in range(start, end) if i != j])
            # 書き込み
            text = "\n".join(context)
            with open("contexts.txt", "a") as wf:
                wf.write(text)


if __name__ == "__main__":
    main()
