from math import log, sqrt
from random import randint, random, uniform


def gen_bernoulli(p: float):
    u = random()
    if u < p:
        return 1
    return 0


def gen_uniform(a: int, b: int, discrete=False):
    if discrete:
        return randint(a, b)
    return uniform(a, b)


def gen_exp(l):
    u = random()
    return  -1 * log(u) / l


def gen_normal(mean=0, var=1):

    while True:
        y1 = gen_exp(1)
        y2 = gen_exp(1)

        y = y2 - (y1 - 1)*(y1 - 1) / 2
        if y > 0:
            u = random()
            z = y1 if u <= 1/2 else -y1
            return mean + sqrt(var) * z
