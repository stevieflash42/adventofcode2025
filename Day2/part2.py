
print("Running Day2.Part2...")

import os
import math

#define everything
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

#read everything in
arRanges = []
with open(file_path, "r") as file:
    currentLine = file.readline()
    while currentLine:
        currentLine = currentLine.strip()
        arStrRanges = currentLine.split(",")
        for strRange in arStrRanges:
            arStrRange = strRange.split("-")
            start = int(arStrRange[0])
            end = int(arStrRange[1])
            arRanges.append(Range(start, end))
        currentLine = file.readline()

invalidTotal = 0
for range in arRanges:
    # print("range: " + str(range.start) + " " + str(range.end))
    currentPart = 1

    useThisLength = len(str(range.end))
    if useThisLength % 2 == 1:
        useThisLength += 1
    finalPart = math.ceil(range.end / (math.pow(10, (useThisLength / 2) - 1)))

    arAlreadyAdded = []
    while currentPart <= finalPart:
        strCurrentPart = str(currentPart)
        expandCurrentPartBy = 2
        current = int(strCurrentPart * expandCurrentPartBy)
        while current <= range.end:
            if current >= range.start and current not in arAlreadyAdded:
                # print("\tadding: " + str(current))
                invalidTotal += current
                arAlreadyAdded.append(current)
            expandCurrentPartBy += 1
            current = int(strCurrentPart * expandCurrentPartBy)

        currentPart += 1


print(str(invalidTotal))
