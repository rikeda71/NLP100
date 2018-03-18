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


def main():
    expdataname = "wordsimilarity_353.csv"
    print("get vectors...")
    # 次元圧縮したベクトルを取得
    global words
    with open("../09/matrix_x.txt", "r") as f:
        words = [word.replace("\n", "") for word in f.readlines()]
    # ベクトルの用意
    global ppmi_vec, w2v_vec
    ppmi_vec = io.loadmat("../09/matrix_300.mat")["a"]
    w2v_vec = models.Word2Vec.load("word2vec_model")
    print("get evaluation data...")
    # 実験データの用意
    with open(expdataname, "r") as f:
        data = [line.replace("\n", "") for line in f.readlines()][1:]

    print("exec anology score...")
    new_text_ppmi = ""
    new_text_w2v = ""
    # 類似度の導出
    for line in tqdm(data):
        split = line.split(",")
        try:
            # ppmi similarity
            one = words.index(split[0])
            two = words.index(split[1])
            ppmi_result = cos_sim_val(ppmi_vec[one], ppmi_vec[two])
            # word2vec similarity
            w2v_result = w2v_vec.wv.similarity(split[0], split[1])
            new_text_ppmi += line + "," + str(ppmi_result) + "\n"
            new_text_w2v += line + "," + str(w2v_result) + "\n"
        except:
            new_text_ppmi += line + ",-1\n"
            new_text_w2v += line + ",-1\n"

    print("save result...")
    # 結果の保存
    with open("ppmi_" + expdataname, "w") as f:
        f.write(new_text_ppmi[:-1])
    with open("w2v_" + expdataname, "w") as f:
        f.write(new_text_w2v[:-1])


if __name__ == "__main__":
    main()
