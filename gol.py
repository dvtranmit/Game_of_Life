import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import options
import gol_utils as utils
import copy
import time
import h5py

print "Welcome to Game of Life"

#importing numx and numy from options.py
options = options.options() #instantiates "options" object from "options" module and assigns it to options
options.parseArguments()

#pulls attributes from options class
numx = options.numx
numy = options.numy
numsteps = options.numsteps
numsleep = options.numsleep
outputfile = options.outputfile
inputfile = options.inputfile

#checks if an input file has been given
if inputfile == "":
    board = rand.rand(numx, numy) #creates a board of random numbers            between (inclusive) and #1 (noninclusive)


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

    f = h5py.File(outputfile)
    f.attrs["Number of Timesteps"] = numsteps
    f.attrs["Sleep Time"] = numsleep
    f.attrs["Number of Rows"] = numy
    f.attrs["Number of Columns"] = numx

    sb = f.create_group("Timestep 0") #sb means seed board
    sb.create_dataset ("Board", data = board)


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
      
        nb = f.create_group("Timestep %d" %(t+1))
        nb.create_dataset ("Board", data = board) 

    f.close()

#runs if input file is given
else:
    #reads input file to define variables
    f = h5py.File(inputfile)
    numsteps = f.attrs["Number of Timesteps"]
    numsleep = f.attrs["Sleep Time"]

    #creates groups
    groups = list(f)

    #creates blank plot for game of life
    plt.ion()
    board = f[groups[0]]['Board'][...]
    img = plt.imshow(np.transpose(board), cmap="hot", animated = True, interpolation = "nearest")
    plt.title("Game of Life")
    plt.draw()

    #runs through groups to display time steps
    for group in groups[1:]:
        plt.imshow(np.transpose(f[group]['Board'][...]), cmap = "hot", interpolation = "nearest")
        plt.draw()
        time.sleep(numsleep)
    #closes file
    f.close()


