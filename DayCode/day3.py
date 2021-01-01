def runCode():
    inputFile = open ('DayCode/Inputs/day3Input.txt', 'r')
    lines = inputFile.readlines()

    slopeList = [1, 3, 5, 7]

    product = 1
    for slope in slopeList:
        lat = 0
        numTrees = 0
        for line in lines:

            if lat >= len(line.rstrip()):
                lat -= len(line.rstrip())

            char = line[lat]
            if char == '#':
                numTrees += 1
                print(line[:lat] + 'X' + line[lat+1:].rstrip() + "  ==  Lat: " + str(lat))
            else:
                print(line[:lat] + 'O' + line[lat+1:].rstrip() + "  ==  Lat: " + str(lat))
            lat += slope
        print("Number of trees hit for slope 1/" + str(slope) + ": " + str(numTrees))
        product *= numTrees
        print("Product: " + str(product))


    lineNum = -1
    slope = 1
    lat = 0
    numTrees = 0
    for line in lines:
        lineNum += 1
        if lineNum % 2 == 0:

            if lat >= len(line.rstrip()):
                lat -= len(line.rstrip())

            char = line[lat]
            if char == '#':
                numTrees += 1
                print(line[:lat] + 'X' + line[lat + 1:].rstrip() + "  ==  Lat: " + str(lat))
            else:
                print(line[:lat] + 'O' + line[lat + 1:].rstrip() + "  ==  Lat: " + str(lat))
            lat += slope
        else:
            print(line.rstrip())
    print("Number of trees hit for slope 2: " + str(numTrees))
    product *= numTrees
    print("Product: " + str(product))