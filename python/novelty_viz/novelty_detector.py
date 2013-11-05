import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import svm

plt.ion()

DURATION = 180

def generator():
    z = np.random.normal

    start = time.time()
    center = (2, 2)
    while start + DURATION > time.time():

        mode = int(time.time() / 15) % 4
        x = z() * 0.2 + center[0]
        y = z() * 0.2 + center[1]

        if mode in (2, 3):
            x = -x
        if mode in (1, 2):
            y = -y

        yield (x, y)

        time.sleep(0.01)

class Novelty(object):

    def __init__(self, variable_count, train_depth=20, threshold=0.3):
        self.stage = 0
        self.variable_count = variable_count
        self.train_depth = train_depth
        self.clear()

        self.idx = 0
        self.clf = None
        self.threshold = threshold
        self.rate = None

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
            raise NewModel()

        if self.stage >= 2:
            self.predict(data)

        if self.stage == 2:
            self.stage += 1

        if self.stage == 3:
            self.rate = float(np.sum(self.normal)) / self.train_depth
            if self.rate < self.threshold:
                print("Relearning: hit rate dropped to %s" % self.rate)
                self.stage = 0
                self.clear()
                raise InvalidModel()

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


class NoveltyException(Exception):
    pass


class InvalidModel(Exception):
    pass


class NewModel(Exception):
    pass


def update_title(ax, msg):
    if not msg == ax.get_title():
        print msg
        ax.set_title(msg)


def main():
    x = []
    y = []


    lim = 4
    xx, yy = np.meshgrid(np.linspace(-lim, lim, 500), np.linspace(-lim, lim, 500))
    boundary = None

    n = Novelty(variable_count=2)
    fig, ax = plt.subplots(1,1)

    a, = ax.plot(x, y, "x", color="blue")
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    rate = plt.text(0, 0, s='')

    for g in generator():

        try:
            n.new(g)
            if n.stage == 0:
                update_title(ax, "Gathering Data for a Model")
            elif n.stage >= 2:
                update_title(ax, "Tracking Expected Behaviour")
        except NewModel:
            update_title(ax, "New Behaviour Model Created")
            Z = n.clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            if boundary:
                ax.clear()
                a, = ax.plot(x, y, "x", color="blue")
                rate = plt.text(0, 0, s='')
            boundary = ax.contour(xx, yy, Z, levels=[0, Z.max()], colors='red')

        except InvalidModel:

            x = []
            y = []
            ax.clear()
            rate = plt.text(0, 0, s='')
            update_title(ax, "Behaviour No Longer Matches the Model")
            a, = ax.plot(x, y, "x", color="blue")

        try:
            msg = "Hit Rate: %s%%" % (n.rate * 100)
        except TypeError:
            msg = "N/A"
        rate.set_text(msg)

        x.append(g[0])
        y.append(g[1])
        a.set_data(x, y)

        plt.draw()
        plt.pause(0.0001)


if __name__ == '__main__':
    main()
