def runCode():
    import string
    inputFile = open ('DayCode/Inputs/day4input.txt', 'r')
    lines = inputFile.readlines()

    validPP = 0
    hasBYR = False
    hasIYR = False
    hasEYR = False
    hasHGT = False
    hasHCL = False
    hasECL = False
    hasPID = False
    eyeColors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    for line in lines:
    #line = lines[5]
    #if True:
        #print(line)
        if line.rstrip() == "":
            #print("Checking " + str(hasBYR) + str(hasIYR) + str(hasEYR) + str(hasHGT) + str(hasHCL) + str(hasECL) + str(hasPID))
            if hasBYR and hasIYR and hasEYR and hasHGT and hasHCL and hasECL and hasPID:
                validPP += 1
            hasBYR = False
            hasIYR = False
            hasEYR = False
            hasHGT = False
            hasHCL = False
            hasECL = False
            hasPID = False
        else:
            items = line.split(" ")
            for item in items:
                fieldName = item[:item.find(":")]
                if fieldName == "byr":
                    value = item[item.find(":")+1:].rstrip()
                    if 1920 <= int(value) <= 2002:
                        hasBYR = True
                elif fieldName == "iyr":
                    value = item[item.find(":") + 1:].rstrip()
                    if 2010 <= int(value) <= 2020:
                        hasIYR = True
                elif fieldName == "eyr":
                    value = item[item.find(":") + 1:].rstrip()
                    if 2020 <= int(value) <= 2030:
                        hasEYR = True
                elif fieldName == "hgt":
                    value = item[item.find(":") + 1:].rstrip()
                    if value[-2:].rstrip() == "in":
                        if 59 <= int(value[:-2]) <= 76:
                            hasHGT = True
                    elif value[-2:].rstrip() == "cm":
                        if 150 <= int(value[:-2]) <= 193:
                            hasHGT = True
                elif fieldName == "hcl":
                    value = item[item.find(":") + 1:].rstrip()
                    if value[0] == "#" and len(value[1:]) == 6:
                        if all(c in string.hexdigits for c in value[1:]):
                            hasHCL = True
                elif fieldName == "ecl":
                    value = item[item.find(":") + 1:].rstrip()
                    if value in eyeColors:
                        hasECL = True
                elif fieldName == "pid":
                    value = item[item.find(":") + 1:].rstrip()
                    if len(value) == 9 and value.isdigit():
                        hasPID = True
    #print("Checking " + str(hasBYR) + str(hasIYR) + str(hasEYR) + str(hasHGT) + str(hasHCL) + str(hasECL) + str(hasPID))
    if hasBYR and hasIYR and hasEYR and hasHGT and hasHCL and hasECL and hasPID:
        validPP += 1
    print("Valid PP: " + str(validPP))