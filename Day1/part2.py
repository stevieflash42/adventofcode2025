print("Running Day1.Part2...")

from enum import Enum
import os

# define everything
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class Rotation:
    def __init__(self, direction: Direction, ticks: int):
        self.direction = direction
        self.ticks = ticks


# read everything in
rotations = []
with open(file_path, "r") as file:
    currentLine = file.readline()
    while currentLine:
        currentLine = currentLine.strip()
        theDirection = (
            Direction.LEFT if currentLine.startswith("L") else Direction.RIGHT
        )
        rotations.append(Rotation(theDirection, int(currentLine[1:])))
        currentLine = file.readline()


# process the rotations
nCurrent = 50
nTimesInclude0 = 0
for r in rotations:

    bStartedAt0 = nCurrent == 0

    nTimesInclude0 += int(r.ticks / 100)
    nTicks = r.ticks % 100

    if r.direction is Direction.LEFT:
        nCurrent -= nTicks
    else:
        nCurrent += nTicks

    # print("\t" + str(r.direction))

    if nCurrent >= 100:
        nCurrent -= 100
        nTimesInclude0 += 1
        # print("\t1")
    elif nCurrent < 0:
        nCurrent += 100
        if not bStartedAt0:
            nTimesInclude0 += 1
            # print("\t1")
    elif nCurrent == 0:
        nTimesInclude0 += 1
        # print("\t1")

    # print(nCurrent)

print(nTimesInclude0)
