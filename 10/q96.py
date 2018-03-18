from gensim import models


class CountryVectors(object):
    """
    word2vecで取得したベクトルのうち
    国名のベクトルを取得するクラス
    self.vectorsが国名のベクトルを持った変数なので，
    クラスを呼び出して変数のみを取得して使う
    """

    def __init__(self):
        # 略称も含めた国名リストから国名を読み込む
        with open("countries_10.txt", "r") as f:
            countries = [line.replace("\n", "") for line in f.readlines()][:-1]
        model = models.Word2Vec.load("word2vec_model")
        vec_dict = {}
        # 国名のベクトルを取得
        for country in countries:
            try:
                vec_dict[country] = model.wv[country]
                if len(country) == 2:
                    c = country[0] + "." + country[1]
                    vec_dict[c] = model.wv[c]
            except:
                pass
        self.vectors = vec_dict


if __name__ == "__main__":
    vec_class = CountryVectors()
    vectors = vec_class.vectors
    print(vectors["Japan"])
