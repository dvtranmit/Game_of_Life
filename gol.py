import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import options
import gol_utils as utils
import copy
import time
import h5py

print "Welcome to Game of Life"

#Instantiates "options" object from "options" module and assigns it to options
options = options.options()

#Gave the user multiple options to modify attributes for the simulation
options.parseArguments()

#The following attributes are imported from options class in options module
numx = options.numx
numy = options.numy
numsteps = options.numsteps
numsleep = options.numsleep
outputfile = options.outputfile
inputfile = options.inputfile



if inputfile == "": #Checks if an input file has been given,

    board = rand.rand(numx, numy) #Seeds a board with random numbers            
                                  #between (inclusive) and #1 (noninclusive)


    for i in range(numx):     #Rounds numbers to 0 or 1
        for j in range(numy):
            if board[i,j] >= 0.5:
                board[i,j] = 1
            else:
                board[i,j] = 0

    old_board = copy.deepcopy(board) #Makes a copy of the old board

    plt.ion() #Turns interactive mode on

    img = plt.imshow(np.transpose(board),        #
                     cmap="hot",                 #Creates black & white colorbar
                     animated = True,            #Turns animated mode on
                     interpolation = "nearest")  #Switches off automatic smoothing 
                                                 #for more definition between cells 


    plt.title("Game of Life")                    #Adds title to matplotlib figure
    plt.draw()                                   #Shows the board

    f = h5py.File(outputfile)                    #Opens HDF5 file
    f.attrs["Number of Timesteps"] = numsteps    #Creates timestep attribute
    f.attrs["Sleep Time"] = numsleep             #Creates sleep time attribute
    f.attrs["Number of Rows"] = numy             #Creates row attribute
    f.attrs["Number of Columns"] = numx          #Creates column attribute

    sb = f.create_group("Timestep 0")            #sb means seed board
    sb.create_dataset ("Board", data = board)    #Creates dataset that takes data   
                                                 #from the seed board


    for t in range(numsteps):
   
        old_board = copy.deepcopy(board) #Makes a copy of the old board

    ###Loops over and determines the fate of each cell using Game of Life Rules###
        for i in range(numx):
            for j in range(numy):

                #Counts the number of alive neighbors
                num_alive = utils.get_num_alive_neighbors(old_board, i, j)
        
 
                if old_board[i,j] == 1:
                    if num_alive < 2:   #Dies if it has less than 2 alive neighbors
                        board[i,j] = 0      
                    elif num_alive > 3: #Dies if it has more than 3 alive neighbors
                        board[i,j] = 0
                elif old_board[i,j] == 0:
                    if num_alive == 3:  #Revived if it has exactly 3 alive neighbors
                        board[i,j] = 1
        
        #See above
        plt.imshow(np.transpose(board), 
                   cmap = "hot",
                   interpolation = "nearest")
        plt.draw()
        time.sleep(numsleep)
        del old_board
        
        #Creates data group for each timestep
        nb = f.create_group("Timestep %d" %(t+1))

        #Adds data from board at that timestep to its respective data group
        nb.create_dataset ("Board", data = board) 

    f.close()    #Closes File "f"

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


