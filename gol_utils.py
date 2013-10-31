def get_num_alive_neighbors(array, i, j): #counts number of alive neighbors

    numx = array.shape[0] #assigns value of x-dimension (index 0) to numx
    numy = array.shape[1] #assigns value of y-dimension (index 1) to numy

    counter = 0 #initiates variable to count alive cells
    
    #all cells not on edge
    if i > 0 and j > 0 and i < numx - 1 and j < numy - 1:
        if array[i-1, j-1] == 1: #top left
            counter += 1
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array[i-1, j+1] == 1: #bottom left
            counter += 1
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
        if array[i+1, j-1] == 1: #top right
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1
        if array[i+1, j+1] ==1: #bottom right
            counter +=1
    
    #top left corner of board
    elif i == 0 and j == 0:
        if array[i+1, j] == 1: #middle right
            counter += 1
        if array[i+1, j+1] == 1: #bottom right
            counter +=1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
    
    #bottom left corner of board
    elif i == 0 and j == numy - 1: 
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i+1, j-1] == 1: #top right
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1
    
    #top right corner of board
    elif i == numx - 1 and j == 0:
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array[i-1, j+1] == 1: #bottom left
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1

    #bottom right corner of board
    elif i == numx - 1 and j == numy - 1: 
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i-1, j-1] == 1: #top left
            counter += 1
        if array[i-1, j] == 1: #middle left
            counter += 1
    
    #left edge of board
    elif i == 0 and j > 0 and j < numy - 1: 
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
        if array[i+1, j-1] == 1: #top right
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1
        if array[i+1, j+1] == 1: #bottom right
            counter +=1
    
    #right edge of board
    elif i == numx - 1 and j > 0 and j < numy -1: 
        if array[i-1, j-1] == 1: #top left
            counter += 1
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array[i-1, j+1] == 1: #bottom left
            counter += 1
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1

    #top edge of board
    elif i > 0 and i < numx - 1 and j == 0: 
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array[i-1, j+1] == 1: #bottom left
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1
        if array[i+1, j+1] == 1: #bottom right
            counter +=1

    #bottom edge of board
    elif i > 0 and i < numx - 1 and j == numy - 1: 
        if array[i-1, j-1] == 1: #top left
            counter += 1
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i+1, j-1] == 1: #top right
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1

    #prints error message in case user entered negative board length or something
    else:
        print "Error: index invalid."
    
    return counter
