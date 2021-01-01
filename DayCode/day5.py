def runCode():
    inputFile = open ('DayCode/Inputs/day5Input.txt', 'r')
    lines = inputFile.readlines()

    maxSeatNum = 0
    seatIDList = []
    #print lines[1]
    #print lines[28]
    for line in lines:
    #if True:
        line = line.rstrip()
        rowSection = line[:7]
        #print(line)
        #print(rowSection)
        rowNumBack = 127
        rowNumFront = 0
        rowNum = 0
        for char in rowSection:
            #print("RowNumBack: " + str(rowNumBack) + " AND RowNumFront: " + str(rowNumFront))
            if char == "F":
                num = rowNumBack - rowNumFront
                halfNum = num / 2
                rowNumBack -= halfNum
            elif char == "B":
                num = rowNumBack - rowNumFront
                halfNum = num / 2
                rowNumFront += halfNum
        #print(rowSection[-1])
        if rowSection[-1] == "F":
            rowNum = rowNumFront+1
        else:
            rowNum = rowNumBack
        #rowNum -= 1
        #print("Row Number: " + str(rowNum))
        seatSection = line[7:]
        #print(seatSection)
        seatNumLeft = 0
        seatNumRight = 8
        seatNum = 0
        for char in seatSection:
            #print("seatNumLeft: " + str(seatNumLeft) + " AND seatNumRight: " + str(seatNumRight))
            if char == 'R':
                num = seatNumRight - seatNumLeft
                halfNum = num / 2
                seatNumLeft += halfNum
            elif char == 'L':
                num = seatNumRight - seatNumLeft
                halfNum = num / 2
                seatNumRight -= halfNum
        if seatSection[-1] == 'L':
            seatNum = seatNumLeft
        else:
            seatNum = seatNumRight-1
        #seatNum -= 1
        #print("Seat Number: " + str(seatNum))
        seatID = rowNum * 8
        seatID += seatNum
        #print("Seat ID: " + str(seatID))
        if seatID > maxSeatNum:
            maxSeatNum = seatID
        seatIDList.append(seatID)
    print("Max Seat ID: " + str(maxSeatNum))
    #print(seatIDList)
    for x in range(int(maxSeatNum)):
        if x in seatIDList:
            pass
        else:
            if x+1 in seatIDList and x-1 in seatIDList:
                print("Your seat is: " + str(x))