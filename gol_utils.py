def get_num_alive_neighbors(array, i, j):

    numx = array.shape[0]
    numy = array.shape[1]

    counter = 0
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
    elif i == 0 and j == 0: #top left corner of board
        if array[i+1, j] == 1: #middle right
            counter += 1
        if array[i+1, j+1] == 1: #bottom right
            counter +=1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
    elif i == 0 and j == numy - 1: #bottom left corner of board
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i+1, j-1] == 1: #top right
            counter += 1
        if array[i+1, j] == 1: #middle right
            counter += 1
    elif i == numx - 1 and j == 0: #top right corner of board
        if array[i-1, j] == 1: #middle left
            counter += 1
        if array[i-1, j+1] == 1: #bottom left
            counter += 1
        if array[i, j+1] == 1: #bottom middle
            counter += 1
    elif i == numx - 1 and j == numy - 1: #bottom right corner of board
        if array [i, j-1] == 1: #top middle
            counter += 1
        if array[i-1, j-1] == 1: #top left
            counter += 1
        if array[i-1, j] == 1: #middle left
            counter += 1
    elif i == 0 and j > 0 and j < numy - 1: #left edge of board
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
    elif i == numx - 1 and j > 0 and j < numy -1: #right edge of board
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
    elif i > 0 and i < numx - 1 and j == 0: #top edge of board
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
    elif i > 0 and i < numx - 1 and j == numy - 1: #bottom edge of board
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
    else:
        print "Error: index invalid."

    return counter
