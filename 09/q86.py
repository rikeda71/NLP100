from scipy import io


def main():
    # 次元圧縮した行列を取得
    with open("matrix_x.txt", "r") as f:
        words = [word[:-1] for word in f.readlines()]
    vectors = io.loadmat("matrix_300.mat")["a"]
    # United Statesのベクトルを表示
    index = words.index("United_States")
    print(vectors[index])


if __name__ == "__main__":
    main()
