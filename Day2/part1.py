
print("Running Day2.Part1...")

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
    useThisLength = len(str(range.start))
    if useThisLength % 2 == 1:
        useThisLength += 1
    initial = math.floor(range.start / (math.pow(10, (useThisLength / 2))))
    
    currentPart = initial
    nextVal = int(str(currentPart) + str(currentPart))
    while nextVal <= range.end:
        if nextVal >= range.start:
            invalidTotal += nextVal
        currentPart += 1
        nextVal = int(str(currentPart) + str(currentPart))


print(str(invalidTotal))
