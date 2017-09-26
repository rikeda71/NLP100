# -*- coding: utf-8 -`*-
import re


def parse_country_names(sentence: str, countries: list) -> str:
    """
    国名が見つかったら国名のスペースを"_"に置換
    """
    for country in countries:
        # 国名が見つからなくなるまで
        while True:
            if sentence.find(country) < 0:
                break
            p = re.search(country, sentence).span()
            sentence = sentence[:p[0]] + sentence[p[0]: p[1]].replace(" ", "_") + sentence[p[1]:]
    return sentence


def main():
    # 国名リストを格納
    with open("countries.txt", "r") as f:
        countries = [country[:-1] for country in f.readlines() if country.find(" ") > -1]
    # 整形した文章を取得
    sentences = []
    with open("tokens.txt", "r") as f:
        sentences = [parse_country_names(sentence, countries) for sentence in f.readlines()]
    # メモリ解放
    del countries

    with open("tokens_81.txt", "w") as f:
        f.write("".join(sentences))


if __name__ == "__main__":
    main()
