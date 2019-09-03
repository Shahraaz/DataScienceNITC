import matplotlib.pyplot as plt
from functools import partials

def dx(f,x,h):
    return (f(x+h)-f(x))/h

def square(x):
    return x*x

def derivative(x):
    return 2*x

derivative_estimat = partials(dx,square,h=0.0001)
x = range(-10,10)
plt.title("Actual Dericactive cs estimates")
plt.plot(x,map(derivative,x),'rx',label='Actual')
plt.plot(x, map(derivative_estimat, x), 'b+', label='Actual')
plt.legend(loc=9)
plt.show()