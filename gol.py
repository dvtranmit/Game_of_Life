import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import options
import gol_utils as utils
import copy
import time

print "Welcome to Game of Life"

#importing numx and numy from options.py
options = options.options()
options.parseArguments()
numx = options.numx
numy = options.numy
numsteps = options.numsteps
numsleep = options.numsleep

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

#creates blank plot for game of life
plt.ion()
img = plt.imshow(np.transpose(board), cmap="hot", animated = True, interpolation = "nearest")
plt.title("Game of Life")
plt.draw()


#counts alive neighbors
for t in range(numsteps):
    old_board = copy.deepcopy(board) #makes a copy of the old board
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
    
    plt.imshow(np.transpose(board), cmap = "hot", interpolation = "nearest")
    plt.draw()
    time.sleep(numsleep)
    del old_board




