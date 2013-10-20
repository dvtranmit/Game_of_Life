import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import options
import gol_utils as utils
import copy

print "Welcome to Game of Life"

#importing numx and numy from options.py
options = options.options()
options.parseArguments()
numx = options.numx
numy = options.numy

board = rand.rand(numx, numy) #creates a board of random numbers between 0 (inclusive) and 
                              #1 (noninclusive)

#seeding the initial state for Game of Life
for i in range(numx): #rounds numbers to 0 or 1
    for j in range(numy):
        if board[i,j] >= 0.5:
            board[i,j] = 1
        else:
            board[i,j] = 0

old_board = copy.deepcopy(board) #makes a copy of the old board

#counts alive neighbors
for i in range(numx):
    for j in range(numy):
        num_alive = utils.get_num_alive_neighbors(old_board, i, j)
        if old_board[i,j] == 1:
            if num_alive < 2:
                board[i,j] = 0
            elif num_alive > 3:
                board[i,j] = 0
        elif old_board[i,j] == 0:
            if num_alive == 3:
                board[i,j] = 1
        

fig = plt.figure()
plt.imshow(np.transpose(board), cmap="hot")
plt.title("Game of Life")
plt.show()
