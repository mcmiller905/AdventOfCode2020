def runCode():
    inputFile = open ('DayCode/Inputs/day10Input.txt', 'r')
    lines = inputFile.readlines()

    numList = []
    for line in lines:
        numList.append(int(line.rstrip()))

    numList.sort()
    print(numList)
    oneDiffs = 1
    threeDiffs = 1
    for x in range(len(numList)-1):
        num = numList[x]
        diff = numList[x+1] - num
        if diff == 1:
            oneDiffs += 1
        elif diff == 3:
            threeDiffs += 1
    print("One Jumps: " + str(oneDiffs))
    print("Three Jumps: " + str(threeDiffs))
    print("ANS: " + str(oneDiffs * threeDiffs))