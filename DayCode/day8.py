def runCode():
    inputFile = open ('DayCode/Inputs/day8Input.txt', 'r')
    lines = inputFile.readlines()

    acc = 0
    listOfJMPanNOP = []
    timesThru = 0
    buildJmpList = True
    weDidIt = False
    while True:
        if weDidIt:
            break
        acc = 0
        listOfRunLines = []
        i = 0
        timesThru += 1
        changeLine = 0;
        if len(listOfJMPanNOP) > 0:
            buildJmpList = False
            changeLine = listOfJMPanNOP[-timesThru]
        while True:
        #print("get line " + str(i))
            if i >= len(lines):
                weDidIt = True
                break
            line = lines[i].rstrip()
            listOfRunLines.append(i)
            command = line[:line.find(" ")]
            arg = int(line[line.find(" ")+1:])
            #print(line)
            if command == "acc":
                acc += arg
                i += 1;
            elif command == "jmp":
                if buildJmpList:
                    listOfJMPanNOP.append(i)
                if i == changeLine:
                    i += 1
                else:
                    if i+arg in listOfRunLines:
                        print("Broke")
                        break
                    else:
                        i += arg
            else:
                if buildJmpList:
                    listOfJMPanNOP.append(i)
                if i == changeLine:
                    if i+arg in listOfRunLines:
                        print("Broke")
                        break
                    else:
                        i += arg
                else:
                    i+=1
            #print(acc)
    print("Not Broke")
    print("Terminated acc: " + str(acc))