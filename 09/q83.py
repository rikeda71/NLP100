# -*- coding: utf-8 -*-
from collections import Counter
import gc


def count_element(dic: dict, counter: list):
    """
    カウントした要素を辞書に反映
    """
    for elem in counter:
        if elem[0] not in dic:
            dic[elem[0]] = int(elem[1])
        else:
            dic[elem[0]] += int(elem[1])


def main():
    # 各値を格納する辞書を用意
    # 共起回数
    cooc_dic = {}
    # 単語の出現回数
    word_dic = {}
    # 文脈語の出現回数
    cont_dic = {}

    # 単語と文脈語のペアの総出現回数を格納する変数
    N = 0
    with open("contexts_light.txt", "r") as f:
        cooc_list = []
        word_list = []
        cont_list = []
        for context in f.readlines():
            N += 1
            # 単語と文脈語に分割
            split = context.split("\t")
            word = split[0]
            cont = split[1]
            # リストに格納
            cooc_list.append(context[:-1])
            word_list.append(word)
            cont_list.append(cont[:-1])
            # 10000文ごとにカウントしていく
            if N % 10000 == 0:
                # 共起，単語，文脈語の出現回数をカウント
                count_element(cooc_dic, Counter(cooc_list).most_common())
                count_element(word_dic, Counter(word_list).most_common())
                count_element(cont_dic, Counter(cont_list).most_common())
                # リセット
                cooc_list = []
                word_list = []
                cont_list = []

        del cooc_list
        del word_list
        del cont_list
        gc.collect()
        # 出現回数で降順ソートして保存
        text = [k + " " + str(v) for k, v in sorted(cooc_dic.items(), key=lambda x: -x[1])]
        with open("q83/cooc.txt", "w") as f:
            f.write("\n".join(text))

        text = [k + " " + str(v) for k, v in sorted(word_dic.items(), key=lambda x: -x[1])]
        with open("q83/word.txt", "w") as f:
            f.write("\n".join(text))

        text = [k + " " + str(v) for k, v in sorted(cont_dic.items(), key=lambda x: -x[1])]
        with open("q83/cont.txt", "w") as f:
            f.write("\n".join(text))

        with open("q83/N.txt", "w") as f:
            f.write(str(N))


if __name__ == "__main__":
    main()
