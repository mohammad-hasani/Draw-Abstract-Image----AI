from deap import base, creator, tools
from tools import *


class GA(object):
    def __init__(self):
        IND_SIZE = 20

        creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("attr_float", build_individual)
        toolbox.register("individual", tools.initRepeat, creator.Individual,
                         toolbox.attr_float, n=IND_SIZE)
        print(toolbox.individual()[0].p1.x)


def build_individual():
    x1 = np.random.random()
    y1 = np.random.random()
    x2 = np.random.random()
    y2 = np.random.random()
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    line = Line(point1, point2)
    return line