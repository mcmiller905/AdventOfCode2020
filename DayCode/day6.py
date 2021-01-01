def runCode():
    inputFile = open ('DayCode/Inputs/day6Input.txt', 'r')
    lines = inputFile.readlines()

    uniqueLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    totalSum = 0
    for line in lines:
        line = line.rstrip()
        print(line)
        if line == "":
            print("Unique Letters for group: " + str(len(uniqueLetters)))
            totalSum += len(uniqueLetters)
            print(uniqueLetters)
            uniqueLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z']
            #break
        else:
            newList = []
            for char in line:
                if char in uniqueLetters:
                    newList.append(char)
                else:
                    uniqueLetters.append(char)
            uniqueLetters = newList
    print("Unique Letters for group: " + str(len(uniqueLetters)))
    totalSum += len(uniqueLetters)
    print(uniqueLetters)
    uniqueLetters = []
    #break
    print("Total sum: " + str(totalSum))