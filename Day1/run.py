
print("Running Day 1 solution...")

from enum import Enum
import os

#define everything
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Rotation:
    def __init__(self, direction: Direction, ticks: int):
        self.direction = direction
        self.ticks = ticks

#read everything in
rotations = []
with open(file_path, "r") as file:
    currentLine = file.readline()
    while currentLine:
        currentLine = currentLine.strip()
        theDirection = Direction.LEFT if currentLine.startswith("L") else Direction.RIGHT
        rotations.append(Rotation(theDirection, int(currentLine[1:])))
        currentLine = file.readline()


#process the rotations
nCurrent = 50
nTimesHit0 = 0
for r in rotations:
    if r.direction is Direction.LEFT:
        nCurrent -= r.ticks
    else:
        nCurrent += r.ticks

    #normalize
    while nCurrent >= 100:
        nCurrent -= 100
    while nCurrent < 0:
        nCurrent += 100
    
    if nCurrent == 0:
        nTimesHit0 += 1

print(nTimesHit0)
