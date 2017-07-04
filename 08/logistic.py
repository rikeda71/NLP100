import numpy as np
import copy


class Logistic_Regression:

    """
    ロジスティック回帰モデルのクラス
    """

    def __init__(self, vector: list=[], sign: list=[]):
        self.vector = np.array(vector)
        self.sign = sign

    def sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))

    def euclidean_distance(self, new_w, old_w):
        return np.linalg.norm(new_w - old_w)

    def learn(self):
        print("learning...")
        self.w = np.array([0.0] * len(self.vector[0]))
        ep = 0.01
        t = 1
        while True:
            old_w = copy.deepcopy(self.w)
            for i in range(len(self.sign)):
                eta = 1.0 / np.sqrt(t)
                q = self.sigmoid(self.sign[i] * np.inner(self.w.T, self.vector[i]))
                self.w += eta * self.sign[i] * (1 - q) * self.vector[i]
                t += 1
            if self.euclidean_distance(self.w, old_w) < ep:
                print(self.w)
                break

    def get_prob(self, vector: list):
        """
        確率値を返す
        prob >= 0.5 pos
        prob <  0.5 neg
        """

        prob = 0
        for i in range(len(vector)):
            prob += self.w[i] * vector[i]
        return self.sigmoid(prob)

    def get_learn_data(self) -> list:
        return self.w.tolist()

    def input_learn_data(self, learndata: list):
        self.w = np.array(learndata)
