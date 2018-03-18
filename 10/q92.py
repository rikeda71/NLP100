from gensim import models
from scipy import io
import numpy as np
from tqdm import tqdm


def cos_sim_val(v1, v2) -> float:
    """
    cos類似度の導出
    """

    np_v1 = np.array(v1)
    np_v2 = np.array(v2)
    ab = np.dot(np_v1, np_v2)
    a = np.linalg.norm(np_v1)
    b = np.linalg.norm(np_v2)
    sim_val = ab / a / b
    if sim_val != sim_val:
        return 0
    return sim_val


def best_anology_ppmi_vec(one: str, two: str, three: str):
    """
    9章で作成したベクトルにおいて，
    two - one + three のベクトルと
    最も類似度の高い単語と類似度を返す
    """

    vector = ppmi_vec[words.index(two)] -\
        ppmi_vec[words.index(one)] +\
        ppmi_vec[words.index(three)]
    store = {}
    for i in range(len(ppmi_vec)):
        store[words[i]] = cos_sim_val(vector, ppmi_vec[i])
    sorted_store = sorted(store.items(), key=lambda x: x[1], reverse=True)
    return sorted_store[0]


def main():
    print("get vectors...")
    # 次元圧縮したベクトルを取得
    global words
    with open("../09/matrix_x.txt", "r") as f:
        words = [word[:-1] for word in f.readlines()]
    # ベクトルの用意
    global ppmi_vec, w2v_vec
    ppmi_vec = io.loadmat("../09/matrix_300.mat")["a"]
    w2v_vec = models.Word2Vec.load("word2vec_model")
    print("get evaluation data...")
    # 実験データの用意
    with open("fam_evaluation_data.txt", "r") as f:
        data = [line[:-1] for line in f.readlines()]

    print("exec anology score...")
    new_text_ppmi = ""
    new_text_w2v = ""
    # 類似度の導出
    for line in tqdm(data):
        split = line.split(" ")
        try:
            ppmi_result = best_anology_ppmi_vec(split[0], split[1], split[2])
            w2v_result = w2v_vec.wv.most_similar_cosmul(positive=[split[1], split[2]], negative=[split[0]], topn=1)
            new_text_ppmi += line + " " + ppmi_result[0] + " " + str(ppmi_result[1]) + "\n"
            new_text_w2v += line + " " + w2v_result[0][0] + " " + str(w2v_result[0][1]) + "\n"
        except:
            new_text_ppmi += line + "  -1\n"
            new_text_w2v += line + "  -1\n"

    print("save result...")
    # 結果の保存
    with open("ppmi_fam_evaluation_data.txt", "w") as f:
        f.write(new_text_ppmi[:-1])
    with open("w2v_fam_evaluation_data.txt", "w") as f:
        f.write(new_text_w2v[:-1])


if __name__ == "__main__":
    main()
