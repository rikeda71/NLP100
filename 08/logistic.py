import numpy as np


class Logistic_Regression:

    """
    ロジスティック回帰モデルのクラス
    """

    def __init__(self, vector: list=[], sign: list=[]):
        self.vector = np.array(vector)
        self.sign = sign

    def sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))

    def learn(self, val=100):
        self.w = np.array([0.0] * len(self.vector[0]))
        eta = 0.1
        for i in range(1, val + 1):
            a = 0
            old_w = self.w
            for i in range(len(self.sign)):
                y = self.sigmoid(np.inner(old_w, self.vector[i]))
                self.w -= eta * (y - self.sign[i]) * self.vector[i]
            for i in range(len(self.w)):
                a += np.abs(self.w[i] - old_w[i])
            eta *= 0.9
        print(self.w)

    def get_prob(self, vector: list):
        """
        確率値を返す
        prob >= 0.5 pos
        prob <  0.5 neg
        """

        prob = 0
        idx = int(len(self.w) / 2)
        for i in range(len(vector)):
            prob += self.w[i] * vector[i]
            prob += self.w[idx + i] * vector[i]
        return self.sigmoid(prob)

    def get_learn_data(self) -> list:
        return self.w.tolist()

    def input_learn_data(self, learndata: list):
        self.w = np.array(learndata)
