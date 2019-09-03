import math


def B(aplha, beta):
    return math.gamma(aplha)*math.gamma(beta) / math.gamma(aplha+beta)


def beta_pdf(x, aplha, beta):
    if x < 0 or x > 1:
        return 0
    return x ** (aplha-1) * (1-x) ** (beta-1) / B(aplha, beta)


print(beta_pdf(-20, 100, 150))
