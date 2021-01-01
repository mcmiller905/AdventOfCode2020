def runCode():
    inputFile = open('DayCode/Inputs/day1Input.txt', 'r')
    numbers = inputFile.readlines()

    count = 0
    secondCount = 0
    for number in numbers:
        count += 1
        secondCount = 0
        for secondNum in numbers[count:]:
            secondCount += 1
            for thirdNum in numbers[count+secondCount:]:
                if int(number) + int(secondNum) + int(thirdNum) == 2020:
                    print("Number1: " + number + "Number2: " + secondNum + "Number3: " + thirdNum)
                    print("Solution: " + str(int(number) * int(secondNum) * int(thirdNum)))
                    print()