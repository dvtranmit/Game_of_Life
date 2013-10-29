=============================================================================
GAME OF LIFE                VERSION 1                           NOVEMBER 2013
=============================================================================




=============================
AUTHORS & CONTACT INFORMATION
=============================

Stephanie Pavlick -- spavlick@mit.edu
Jasmeet Arora     -- jasmeet@mit.edu
Davis Tran        -- dvtran@mit.edu

==============
BRIEF OVERVIEW
==============

Game of Life is a cellular automata simulation. Game of Life creates a randomized array of dead and alive cells and uses a set of rules to determine whether each cell lives or not after each timestep.

=====
RULES
=====

1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

=======================
DOWNLOAD & INSTALLATION
=======================

Create a directory for the repository

Use the cd command to enter the new directory

Run the following code in the Linux terminal:
    
    git clone https://github.com/dvtranmit/Game_of_Life.git

=======================
HOW TO RUN GAME OF LIFE
=======================

The Game of Life program is stored as "gol.py" in the downloaded repository.

Basic Simulation---------------------------------------------------------

        To run the program without any modifications, use the following command:

        >$ python gol.py

Changing Board Size------------------------------------------------------

        To change the board size of the simulation:

        >$ python gol.py -x "--x-dimension--" -y "--y-dimension--"

        Where the user should replace "--x-dimension--" with the desired x-   
        dimesension of the board and "--y-dimension--" with the desired y-dimension 
        of the board. The user may also change just one parameter by using either 
        command by itself.

        Acceptable Input: Entering anything other than a positive integer 
        may break the program.

Changing Number Of Time Steps--------------------------------------------

        To change the number of time steps of the simulation:

        >$ python gol.py -t "--timesteps--"

        Where the user should replace "--timesteps--" with the desired number of    
        timesteps for the simulation.

        Acceptable Input: Entering anything other than a positive integer may break 
        the program.

Changing Sleep Time-------------------------------------------------------

        To change the sleep times of the simulation:

        >$ python gol.py -s "--sleep time--"

        Where the user should replace "--sleep time--" with the disired sleep time 
        for the simulation.

        Acceptable Input: Entering anything other than a positive integer may break 
        the program.

Storing and Naming HDF5 File Name------------------------------------------

        
