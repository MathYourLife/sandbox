import numpy as np
import matplotlib.font_manager
import matplotlib.pyplot as plt
from sklearn import svm
import json
import sys
import time


class Novelty(object):

    def __init__(self, variable_count, train_depth=20, threshold=0.3):
        self.stage = 0
        self.variable_count = variable_count
        self.train_depth = train_depth
        self.clear()

        self.idx = 0
        self.clf = None
        self.threshold = threshold

    def clear(self):
        self.train_data = np.array([np.nan] * self.train_depth * self.variable_count)
        self.train_data.shape = (self.train_depth, self.variable_count)
        self.normal = np.array([np.nan] * self.train_depth, dtype=np.bool)

    def new(self, data):
        self.idx += 1
        self.idx %= self.train_depth

        if self.stage == 0:
            self.gather_training(data)

        if self.stage == 1:
            self.train()

        if self.stage >= 2:
            self.predict(data)

        if self.stage == 2:
            self.stage += 1

        if self.stage == 3:
            rate = float(np.sum(self.normal)) / self.train_depth
            print rate
            if rate < self.threshold:
                print("Relearning: hit rate dropped to %s" % rate)
                self.stage = 0
                self.clear()

    def gather_training(self, data):
        self.train_data[self.idx] = data
        if np.sum(np.isnan(self.train_data)) == 0:
            self.stage += 1

    def train(self):
        # fit the model
        self.clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
        self.clf.fit(self.train_data)
        self.stage += 1

    def predict(self, data):
        v = self.clf.predict(data)
        self.normal[self.idx] = v > 0



n = Novelty(variable_count=2)


while True:

    line = sys.stdin.readline()
    if not line:
        break

    data = json.loads(line[:-1])

    n.new(data)

