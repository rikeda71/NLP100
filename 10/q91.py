

def main():
    # analogyデータの読み込み
    with open("evaluation_data.txt", "r") as f:
        analogy_dic = {}
        for line in f.readlines():
            if line[0] == ":":
                sec = line[2:-1]
                analogy_dic[sec] = []
            else:
                analogy_dic[sec].append(line[:-1])
    # familyセクションだけ抽出して保存
    text = "\n".join(analogy_dic["family"])
    with open("fam_evaluation_data.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
