# -*- coding: utf-8 -*-
import re
import gc


def main():
    new_sentences = ""
    r = re.compile(r"([.,!\?;:\(\)\[\]\'\"])")
    # ファイル読み込み 後の処理のために改行コードの前に空白を入れる
    with open("enwiki-20150112-400-r100-10576.txt", "r") as f:
        sentences = [sentence[:-1] for sentence in f.readlines()]
    # トークンごとに分割
    i = 0
    for sentence in sentences:
        i += 1
        print(i)
        tokens = sentence.split(" ")
        # いらない文字を削除
        for token in tokens:
            true_token = r.sub("", token)
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
