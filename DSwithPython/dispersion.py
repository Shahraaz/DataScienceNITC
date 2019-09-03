from collections import Counter

num_frintds = [100, 48, 41, 40, 25]


def mean(x):
    return sum(x) / len(x)


def data_range(x):
    return max(x) - min(x)


print(data_range(num_frintds))


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    dev = de_mean(x)
    return sum_of_squares(dev) / (n - 1)


def dot(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def sum_of_squares(x):
    return dot(x, x)

print(de_mean(num_frintds),"Ine")
# print(dot(num_frintds),"Tow")
print(sum_of_squares(num_frintds))
print(variance(num_frintds))
