import numpy as np
import random

x = np.linspace(0, 10, 1001)
a = 4.2
b = 0.666

y = a*x + b
sig_y = 1+0.05*np.abs(y)

randomized_y = []
for i in range(len(y)):
  randomized_y.append(random.gauss(y[i], sig_y[i]))
randomized_y = np.array(randomized_y)

np.savetxt('linearData.xye', np.c_[x,randomized_y,sig_y], fmt='%10.5f')