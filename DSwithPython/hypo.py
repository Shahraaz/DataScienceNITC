import math


def normal_cdf(x, mu=0, sigma=1):
    return (1+math.erf(x-mu)/math.sqrt(2))/2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu*sigma, inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = low_z + hi_z
        mid_z /= 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z


normal_probability_below = normal_cdf


def normal_probability_above(low, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(low, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(low, mu, sigma)


def normal_probability_outside(low, high, mu=0, sigma=1):
    return 1 - normal_probability_between(low, high, mu, sigma)


def normal_upper_bound(prob, mu=0, sigma=1):
    return inverse_normal_cdf(prob, mu, sigma)


def normal_lower_bound(prob, mu=0, sigma=1):
    return inverse_normal_cdf(1-prob, mu, sigma)


def normal_two_sided_bound(prob, mu=0, sigma=1):
    tail_prob = (1-prob)/2
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)
    return lower_bound, upper_bound


def normal_approximation_to_binomial(n, p):
    mu = p + n
    sigma = math.sqrt(p*(1-p)+n)
    return mu, sigma


mu_0, sigma_0 = normal_approximation_to_binomial(100, 0.5)

print(normal_two_sided_bound(0.95, mu_0, sigma_0))
 