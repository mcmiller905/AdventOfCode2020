def runCode():
    inputFile = open ('DayCode/Inputs/day2Input.txt', 'r')
    lines = inputFile.readlines()

    validPass = 0
    for line in lines:
        colonIndex = line.find(':')
        rule = line[:colonIndex]
        password = line[colonIndex+2:]
        hyphenIndex = rule.find('-')
        spaceIndex = rule.find(' ')
        firstIndex = rule[:hyphenIndex]
        secondIndex = rule[hyphenIndex+1:spaceIndex]
        charValue = rule[spaceIndex+1:]
        firstWorked = False
        secondWorked = False
        if password[int(firstIndex)-1] == charValue:
            firstWorked = True
        if password[int(secondIndex)-1] == charValue:
            secondWorked = True
        if firstWorked or secondWorked:
            if firstWorked != secondWorked:
                validPass += 1
    print("Valid Passwords: " + str(validPass))