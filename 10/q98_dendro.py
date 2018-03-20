from q96 import CountryVectors
import numpy as np
from scipy import io
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt


def main():
    cv = CountryVectors()
    w = ward(list(cv.vectors.values()))

    # デンドログラムの描画
    dendrogram(w, labels=list(cv.vectors.keys()), leaf_font_size=5)
    plt.show()


if __name__ == "__main__":
    main()
