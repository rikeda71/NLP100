

def show_anology_score(anology_list: list):
    """
    評価データから正解率を表示する
    """

    correct = 0
    for line in anology_list:
        split = line.split(" ")
        if split[-1] == "-1":
            continue
        elif split[-2] == split[-3]:
            correct += 1
    print("acculacy : " + str(correct / len(anology_list)))


def main():
    with open("ppmi_fam_evaluation_data.txt", "r") as f:
        ppmi = [line.replace("\n", "") for line in f.readlines()]
    with open("w2v_fam_evaluation_data.txt", "r") as f:
        w2v = [line.replace("\n", "") for line in f.readlines()]
    print("ppmi ", end="")
    show_anology_score(ppmi)
    print("w2v  ", end="")
    show_anology_score(w2v)


if __name__ == "__main__":
    main()
