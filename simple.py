import numpy as np
import matplotlib.pyplot as plt
print "Hello World" #lol

import numpy.random as rand

a = rand.rand (50,50)
fig = plt.figure ()
plt.imshow (a)
plt.colorbar()
plt.title("Random Numbers")
plt.show ()


