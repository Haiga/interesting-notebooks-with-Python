import numpy as np
import matplotlib.pyplot as plt


class Force():
    def __init__(self, intensity_x, intensity_y):
        self.intensity_x = intensity_x
        self.intensity_y = intensity_y


class Ball():
    def __init__(self, pos_x: float, pos_y: float, weight: float = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.vec_x = 0
        self.vec_y = 0

        self.weight = weight
        self.forces = []

    def addForce(self, force: Force):
        self.forces.append(force)

    def timeLapse(self, time: float):
        all_forces = np.array(self.forces)

        vec_acc_x = np.vectorize(lambda f: f.intensity_x)
        vec_acc_y = np.vectorize(lambda f: f.intensity_y)

        acc_x = np.sum(vec_acc_x(all_forces))
        acc_y = np.sum(vec_acc_y(all_forces))

        self.vec_x = self.vec_x + acc_x * time
        self.vec_y = self.vec_y + acc_y * time

        self.pos_x = self.pos_x + self.pos_x * time + acc_x * time * time / 2
        self.pos_y = self.pos_y + self.pos_y * time + acc_y * time * time / 2

    def draw(self):
        plt.plot(self.pos_x, self.pos_y, 'o', color='k')


timeInitial = 0
timeFinal = 0.005
timelapse = 0.001

times = np.arange(timeInitial, timeFinal, timelapse)

bs = [
    Ball(2, 2),
    Ball(1, 2),
    Ball(4, 4),
    Ball(3, 1),
]

gravity = Force(0, -9.86)
[b.addForce(gravity) for b in bs]

# plt.show()


for t in times:
    plt.figure()
    for ball in bs:
        ball.timeLapse(t)
        ball.draw()
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.show()
    plt.clf()
