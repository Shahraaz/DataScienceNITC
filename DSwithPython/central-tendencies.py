from collections import Counter

num_frintds = [100, 48, 41, 40, 25]

# Calculating Mean Value
def mean(x):
    return sum(x) / len(x)


print(mean(num_frintds))


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint - 1] + sorted_v[midpoint]) / 2

def quantile(x,p):
    #Calculating Quantile Value
    p_index = int(p*len(x))
    return sorted(x)[p_index]

print(quantile(num_frintds,0.10))

print(median(num_frintds))

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]

print(mode(num_frintds))