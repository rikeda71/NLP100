# -*- coding:utf-8 -*-
import codecs
import random


def add_tag(filename, tag) -> list:
    """
    指定したタグを文頭に着けてリストで返す
    """

    lines = []
    # タグ付けしたテキストを用意
    with codecs.open(filename, 'r', 'cp1252') as f:
        for line in f.readlines():
            lines.append(tag + line)

    return lines


if __name__ == '__main__':
    # ポジネガのタグをつける
    pos = add_tag('rt-polaritydata/rt-polarity.pos', '+1')
    neg = add_tag('rt-polaritydata/rt-polarity.neg', '-1')
    # 結合してシャッフル
    concatenate = pos
    concatenate.extend(neg)
    random.shuffle(concatenate)
    # 書き込み
    with open('sentiment.txt', 'w') as f:
        f.write(''.join(concatenate))
