def runCode():
    inputFile = open ('DayCode/Inputs/day7Input.txt', 'r')
    lines = inputFile.readlines()
    runPart1 = True
    runPart2 = True

    if runPart1:
        #make bag map
        bagMap = {}
        for line in lines:
            line = line.rstrip()
            line = line.replace(" bags", "")
            line = line.replace(" bag", "")
            line = line.replace(".", "")
            splitLine = line.split(" contain ")
            innerBags = splitLine[1]
            bagMap.update({splitLine[0]: splitLine[1]})

        #make bag list
        listOBags = []
        newThingsToCheck = ["shiny gold"]
        while len(newThingsToCheck) != len(listOBags):
            checkList = newThingsToCheck
            for bagToCheck in checkList:
                for key in bagMap.keys():
                    if(bagToCheck in bagMap.get(key)):
                        if key not in newThingsToCheck:
                            newThingsToCheck.append(key)
                        if key not in listOBags:
                            listOBags.append(key)
            newThingsToCheck.remove(bagToCheck)
        print("Part 1:")
        print(len(listOBags))

    if runPart2:
        #make bag map
        bagMap = {}
        for line in lines:
            line = line.rstrip()
            line = line.replace(" bags", "")
            line = line.replace(" bag", "")
            line = line.replace(".", "")
            splitLine = line.split(" contain ")
            innerBags = splitLine[1]
            innerBagList = innerBags[:len(innerBags)-0].split(", ")
            for innerBag in innerBagList:
                if innerBag[0] == '1':
                    innerBag = innerBag + "s"
            bagMap.update({splitLine[0]: innerBagList})
        
        # get inner bags
        totalNumBags = 0
        bagsToCheck = ["1 shiny gold"]
        while(len(bagsToCheck) > 0):
            newBagList = []
            for bag in bagsToCheck:
                parentNum = int(bag[:bag.find(" ")])
                innerBags = []
                for key in bagMap.keys():
                    if bag[bag.find(" ")+1:] in key:
                        innerBags = bagMap.get(key)
                for innerBag in innerBags:
                    if(not innerBag == "no other"):
                        firstSpaceIndex = innerBag.find(" ")
                        num = int(innerBag[:firstSpaceIndex])
                        bagType = innerBag[firstSpaceIndex+1:]
                        totalNumBags += num*parentNum
                        newBagList.append(str(num*parentNum) + " " + bagType)
            bagsToCheck = newBagList
            newBagList = []

        print("Part 2:")
        print(totalNumBags)