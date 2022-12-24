def runCode():
    inputFile = open ('DayCode/Inputs/day11Input.txt', 'r')
    lines = inputFile.readlines()

    grid = lines
    print("START")
    #printGrid(grid)
    for iter in range(300):
        newGrid = []
        for i in range(len(grid)):
            row = grid[i]
            newRow = ""
            for j in range(len(row)):
                seat = row[j]
                if seat == "L":
                    #part 1
                    #numAdj = getAdjSeats(i,j,grid)
                    #part 2
                    numAdj = getVisibleSeats(i,j,grid)
                    if(numAdj == 0):
                        newRow += "#"
                    else:
                        newRow += "L"
                elif seat == "#":
                    #part 1
                    #numAdj = getAdjSeats(i,j,grid)
                    #part 2
                    numAdj = getVisibleSeats(i,j,grid)
                    if(numAdj > 4):
                        newRow += "L"
                    else:
                        newRow += "#"
                else:
                    newRow += "."
            newGrid.append(newRow)
        if grid == newGrid:
            printGrid(grid)
            print("this is it")
            print("total sitters: " + str(countSitters(grid)))
            break
        grid = newGrid
        print(str(iter) + "ITER")
        #printGrid(grid)


def getAdjSeats(i,j,grid):
    #part 1
    numAdj = 0
    # check line before
    if(i-1>=0):
        preLine = grid[i-1]
        if(j-1>=0):
            if(preLine[j-1] == "#"):
                numAdj += 1
        if(preLine[j] == "#"):
            numAdj += 1
        if(j+1 < len(preLine)):
            if(preLine[j+1] == "#"):
                numAdj += 1
    # check same line
    curLine = grid[i]
    if(j-1>=0):
        if(curLine[j-1] == "#"):
            numAdj += 1
    if(j+1<len(curLine)):
        if(curLine[j+1] == "#"):
            numAdj += 1
    # check next line
    if(i+1<len(grid)):
        nextLine = grid[i+1]
        if(j-1>=0):
            if(nextLine[j-1] == "#"):
                numAdj += 1
        if(nextLine[j] == "#"):
            numAdj += 1
        if(j+1 < len(nextLine)):
            if(nextLine[j+1] == "#"):
                numAdj += 1
    return numAdj


def getVisibleSeats(i,j,grid):
    #part 2
    numAdj = 0
    # check line before
    if(i-1>=0):
        preLine = grid[i-1]
        if(j-1>=0):
            if(preLine[j-1] == "#"):
                numAdj += 1
        if(preLine[j] == "#"):
            numAdj += 1
        if(j+1 < len(preLine)):
            if(preLine[j+1] == "#"):
                numAdj += 1
    # check same line
    curLine = grid[i]
    if(j-1>=0):
        if(curLine[j-1] == "#"):
            numAdj += 1
    if(j+1<len(curLine)):
        if(curLine[j+1] == "#"):
            numAdj += 1
    # check next line
    if(i+1<len(grid)):
        nextLine = grid[i+1]
        if(j-1>=0):
            if(nextLine[j-1] == "#"):
                numAdj += 1
        if(nextLine[j] == "#"):
            numAdj += 1
        if(j+1 < len(nextLine)):
            if(nextLine[j+1] == "#"):
                numAdj += 1
    return numAdj


def printGrid(grid):
    for line in grid:
        print(str(line))


def countSitters(grid):
    retval = 0
    for row in grid:
        for seat in row:
            if seat == "#":
                retval += 1
    return retval