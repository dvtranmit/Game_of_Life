import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

print "Welcome to Game of Life"


import options

board = rand.rand(numx, numy) #creates a board of random numbers between 0 (inclusive) and 1 (noninclusive)

for i in range(numx): #rounds numbers to 0 or 1
    for j in range(numy):
        if board[i,j] >= 0.5:
            board[i,j] = 1
        else:
            board[i,j] = 0

fig = plt.figure()
plt.imshow(board, cmap="hot")
plt.title("Game of Life")
plt.show()
