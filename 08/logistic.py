import numpy as np


class Logistic_Regression:

    """
    ロジスティック回帰モデルのクラス
    """

    def __init__(self, vector: list, sign: list):
        self.vector = np.array(vector)
        self.sign = sign

    def sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))

    def learn(self):
        np.random.seed()
        self.w = [0] * len(self.vector[0])
        learn_rate = 0.1
        while True:
            a = 0
            old_w = self.w
            for i in range(len(self.sign)):
                y = self.sigmoid(np.inner(self.vector[i], old_w))
                self.w -= learn_rate * (y - self.sign[i]) * self.vector[i]
            for i in range(len(self.w)):
                a += np.abs(self.w[i] - old_w[i])
            learn_rate += 0.9
            if(np.all(self.w == old_w)):
                break

    def get_pos_prob(self, vector: list):
        prob = 0
        for i in range(len(vector)):
            prob = vector[i] * self.w[i]
        return prob

    def get_neg_prob(self, vector: list):
        prob = 0
        idx = len(self.w) / 2
        for i in range(len(vector)):
            prob = vector[i] * self.w[i]
        return prob

    def get_learn_data(self) -> list:
        return self.w.tolist()

    def input_learn_data(self, learndata: list):
        self.w = learndata
