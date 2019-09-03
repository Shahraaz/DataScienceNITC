from matplotlib import pyplot as plt
from collections import Counter
num_frintds = [100,48,41,40,25]
friends_counts = Counter(num_frintds)
xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()