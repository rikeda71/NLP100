from gensim import models


def main():
    with open("../09/tokens_81.txt", "r") as f:
        sentences = [sentence.replace("\n", "").split(" ") for sentence in f.readlines()]
    model = models.Word2Vec(sentences, sg=1, size=300, window=5, min_count=5, workers=4)
    model.save("word2vec_model")
    # q86
    print("===q86===")
    United_States = model.wv["United_States"]
    print(United_States)
    # q87
    print("===q87===")
    print(model.wv.similarity("United_States", "U.S"))
    # q88
    print("===q88===")
    print(model.wv.most_similar_cosmul(positive=["England"], topn=10))
    # q89
    print("===q89===")
    print(model.wv.most_similar_cosmul(positive=["Spain", "Athens"], negative=["Madrid"], topn=10))


if __name__ == "__main__":
    main()
