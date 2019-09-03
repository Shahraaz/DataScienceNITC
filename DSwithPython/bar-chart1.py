from matplotlib import pyplot as plt
movies = ["Annie Hall","ben-Hur","Caass","Gandhi","WestSide"]
num_oscars = [5,11,3,8,10]
xs = [i+0.1 for i,_ in enumerate(movies)]
plt.bar(xs,num_oscars)
plt.ylabel("# of Oscars")
plt.title("My Favorite Movies")
plt.xticks([i+0.5 for i,_ in enumerate(movies)],movies)
plt.show()