# -*- coding: utf-8 -*-
import re


def main():
    tokens = []
    with open("enwiki-20150112-400-r10-105752.txt", "r") as f:
        sentences = [sentence for sentence in f.readlines()]
    # トークンごとに分割
    for sentence in sentences:
        tokens.extend(sentence.split(" "))
    # いらない文字を削除
    new_sentences = ""
    for token in tokens:
        true_token = re.sub(r"[.,!\?;:\(\)\[\]\'\"]", "", token)
        if true_token != "":
            new_sentences += true_token + " "
    # メモリの解放
    del sentences
    del tokens

    with open("tokens.txt", "w") as f:
        f.write(new_sentences)


if __name__ == "__main__":
    main()
