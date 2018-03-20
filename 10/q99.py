from q96 import CountryVectors
from q97 import k_means
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


def main():
    cv = CountryVectors()
    t = TSNE(n_components=2).fit_transform(list(cv.vectors.values()))

    # クラスタリング(可視化に色をつけて結果があっているか確認するため)
    k = 5
    clusters = k_means(cv.vectors, k)
    dic = {}
    for k, v in clusters.items():
        for name in v:
            dic[name] = k

    # 表示
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('rainbow')
    for index, label in enumerate(cv.vectors.keys()):
        c = cmap(dic[label] / (k - 1))
        ax.scatter(t[index, 0], t[index, 1], marker='.', color=c)
        ax.annotate(label, xy=(t[index, 0], t[index, 1]), color=c)
    plt.show()


if __name__ == "__main__":
    main()
