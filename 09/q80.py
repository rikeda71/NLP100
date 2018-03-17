# -*- coding: utf-8 -*-
import re
import gc


def main():
    new_sentences = ""
    top = re.compile(r"^[.,!\?;:\(\)\[\]\'\"]")
    last = re.compile(r"[.,!\?;:\(\)\[\]\'\"]$")
    # ファイル読み込み 後の処理のために改行コードの前に空白を入れる
    with open("enwiki-20150112-400-r100-10576.txt", "r") as f:
        sentences = [sentence[:-1] for sentence in f.readlines()]
    # トークンごとに分割
    for sentence in sentences:
        tokens = sentence.split(" ")
        # いらない文字を削除
        for token in tokens:
            true_token = top.sub("", token)
            true_token = last.sub("", token)
            if true_token != "":
                new_sentences += true_token + " "
        new_sentences = new_sentences[:-1] + "\n"
    # メモリ解放
    del sentences
    del tokens
    gc.collect()

    with open("tokens.txt", "w") as f:
        f.write(new_sentences)


if __name__ == "__main__":
    main()
