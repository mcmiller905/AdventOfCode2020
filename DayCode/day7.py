def runCode():
    inputFile = open ('DayCode/Inputs/day7Input.txt', 'r')
    lines = inputFile.readlines()

    fakeMap = []
    for line in lines:
    #if True:
        line = line.rstrip()
        parentList = []
        containsIndex = line.find("contain")
        parent = line[:containsIndex].rstrip(" bags ")
        #print parent
        parentList.append(parent)
        childString = line[containsIndex+8:]
        if childString == "no other bags.":
            #print childString
            pass
        else:
            childList = []
            for child in childString.split(', '):
                bagIndex = child.find(" bag")
                childList.append(child[2:bagIndex])
            #print(childList)
            parentList.append(childList)
            if len(fakeMap) == 0:
                fakeMap.append(parentList)
            else:
                inMapFlag = False
                for mapKey in fakeMap:
                    if mapKey[0] == parent:
                        inMapFlag = True
                        for kid in childList:
                            mapKey[1].append(kid)
                if inMapFlag:
                    pass
                else:
                    fakeMap.append(parentList)
    print(fakeMap)
    for parent in fakeMap:
        if "shiny gold" in parent[1]:
            print(parent[0])