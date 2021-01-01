def runCode():
    inputFile = open ('DayCode/Inputs/day9Input.txt', 'r')
    lines = inputFile.readlines()

    numList = []
    for line in lines:
        numList.append(int(line.rstrip()))
    startIndex = 0
    endIndex = 25
    last25 = numList[:25]
    #print(last25)
    keyNum = 0
    for sumNum in numList[25:]:
    #if True:
        #sumNum = numList[25]
        #print(sumNum)
        last25Index = 0
        sumFound = False
        for firstNum in last25:
            #print("First: " + str(firstNum))
            last25Index += 1
            if firstNum < sumNum:
                for secNum in last25[last25Index:]:
                    #print("Sec: " + str(secNum))
                    if firstNum+secNum == sumNum:
                        sumFound = True
        if sumFound:
            startIndex += 1
            endIndex += 1
            last25 = numList[startIndex:endIndex]
        else:
            print("Sum not found: " + str(sumNum))
            keyNum = sumNum
            break

    print("keyNum = " + str(keyNum))
    lowNum = 0
    highNum = 0
    foundIt = False
    for x in range(len(numList)):
        if foundIt:
            break
        num = numList[x]
        sumOfSubList = num
        lowNum = num
        highNum = num
        nextIndex = 1
        while sumOfSubList <= keyNum:
            nextNum = numList[x+nextIndex]
            sumOfSubList += nextNum
            if nextNum < lowNum:
                lowNum = nextNum
            if nextNum > highNum:
                highNum = nextNum
            if sumOfSubList == keyNum:
                print("Found It" + str(sumOfSubList))
                print(nextIndex)
                foundIt = True
                break
            nextIndex += 1
    print("Low num: " + str(lowNum) + " High num: " + str(highNum))
    print("sum=" + str(lowNum + highNum))

