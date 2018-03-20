from q96 import CountryVectors
import numpy as np


def center_of_gravity(c1):
    """
    クラスタ内の重心を求める
    """

    return sum(c1) / len(c1)


def L_val(c):
    """
    クラスタC内での散らばり具合（重心からの距離の2乗和）を返す
    """

    cg = center_of_gravity(c)
    return sum([np.linalg.norm(v - cg) for v in c])


def cluster_distance(c1, c2) -> float:
    """
    2つのクラスタが結合されたときの重心と各クラスタとの距離の2乗和L(P∪Q)
    もともとの2つのクラスタ内での重心とそれぞれのサンプルとの距離の2乗和L(P), L(Q)
    L(P∪Q) - L(P) - L(Q)の値を返す
    """

    p_or_q = c1 + c2
    return L_val(p_or_q) - L_val(c1) - L_val(c2)


def flatten_with_any_depth(nested_list):
    """
    深さ優先探索の要領で入れ子のリストをフラットにする関数
    """

    # フラットなリストとフリンジを用意
    flat_list = []
    fringe = [nested_list]

    while len(fringe) > 0:
        node = fringe.pop(0)
        # ノードがリストであれば子要素をフリンジに追加
        # リストでなければそのままフラットリストに追加
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list


def get_vectors_in_cluster(vectors: dict, tree: list) -> list:
    """
    1つのクラスタに含まれるベクトルの集合を返す
    """

    return [vectors[i] for i in flatten_with_any_depth(tree)]


def ward_analysis(vectors: dict):
    """
    k-means法によるクラスタリングの結果を
    表示する関数
    """

    # ベクトルの数と初期のクラスタ
    c_tree = [k for k in vectors.keys()]

    while len(c_tree) > 2:
        minlen = float("inf")
        n = len(c_tree)
        # すべてのクラスタの組み合わせについて距離の計算をしていく
        for i in range(n - 1):
            for j in range(i + 1, n):
                c1 = get_vectors_in_cluster(vectors, c_tree[i])
                c2 = get_vectors_in_cluster(vectors, c_tree[j])
                length = cluster_distance(c1, c2)
                # 最も距離が短い組み合わせを覚えておく
                if minlen > length:
                    d1 = i
                    d2 = j
                    minlen = length
        # 最も距離が近いクラスタを結合
        new_c = [c_tree[d1], c_tree[d2]]
        c_tree.pop(d2)
        c_tree.pop(d1)
        c_tree.append(new_c)

    print(c_tree)


def main():
    cv = CountryVectors()
    ward_analysis(cv.vectors)


if __name__ == "__main__":
    main()
