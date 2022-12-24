# Advent Of Code 2020 in Python
# Code by mcmiller905@gmail.com
from importlib import import_module
import os, time
# Change dayToRun to the desired Day
dayToRun = 10
run = True

def runDay(dayNum):
    print()
    print("*--------------------")
    print("*  DAY " + str(dayNum))
    print("*--------------------")
    print()
    module = import_module('DayCode.day'+str(dayNum))
    runCode = getattr(module, 'runCode')
    startTime = time.perf_counter()
    answer = runCode()
    endTime = time.perf_counter()
    print(f"Runtime: - {1000 * (endTime - startTime):0.2f}ms")

if(dayToRun == 0):
    numFiles = len(next(os.walk("DayCode"))[2]) + 1
    i = 1
    totalStartTime = time.perf_counter()
    while(i < numFiles):
        runDay(i)
        i+=1
    totalEndTime = time.perf_counter()
    runTime = 1000 * (totalEndTime - totalStartTime)
    runTimeText = f"{runTime:0.2f}ms"
    if(runTime > 1000):
        runTimeText = f"{(runTime/1000):0.2f}s"
    print()
    print(f"Total time: - " + runTimeText)
else:
    runDay(dayToRun)
print()