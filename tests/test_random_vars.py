from src.random_vars import gen_bernoulli, gen_exp, gen_normal, gen_uniform

M = 10000000

def test_bernoulli():
    p = 0.1
    c = 0
    for _ in range(M):
        u = gen_bernoulli(p)
        if u:
            c += 1

    assert abs(c / M - 0.1) < 0.01, "test_bernoulli: Wrong Answer"

    print("test_bernoulli: Accepted")


def test_uniform(_discrete=False):
    mean = 0
    for _ in range(M):
        mean += gen_uniform(1, 10, discrete=_discrete)

    if _discrete:
        mean = mean // M
        assert mean == 5, "test_discrete_uniform: Wrong Answer"
        print("test_discrete_uniform: Accepted")

    else:
        mean = mean / M
        assert abs(5.5 - mean) < 0.01, "test_continuous_uniform: Wrong Answer"
        print("test_continuous_uniform: Accepted")


    

def test_exp():
    mean = 0
    for _ in range(M):
        mean += gen_exp(30)

    mean = mean / M

    assert abs(mean - 1/30) < 0.01

    print("test_exp: Accepted")


def test_normal():
    mean = 0
    var = 0
    for _ in range(M):
        t = gen_normal(10, 5)
        mean += t
        var += (t - 10) * (t - 10)

    mean = mean / M
    var = var / (M-1)

    assert abs(mean - 10) < 0.01 and abs(var - 5) < 0.01

    print("test_normal: Accepted")


def run_tests():
    test_bernoulli()
    test_uniform()
    test_uniform(_discrete=True)
    test_exp()
    test_normal()
