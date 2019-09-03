from matplotlib import pyplot as plt
import numpy as np

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100*np.random.random(20)
xdata = np.random.normal(xdata, 10)
ydata = theta_true[0] + theta_true[1]*xdata

#adding up sactter to points
ydata = np.random.normal(ydata, 10)

plt.plot(xdata,ydata,'ok')
plt.xlabel('x')
plt.xlabel('y')
plt.show()
