TEST_INPUT = "2021/test.txt"
PUZZLE_INPUT = "2021/2021_09.txt"
checkedPos = []
count = 0
def readInput(filename):
    data = []
    init = True
    emptyRow = []
    with open(filename, 'r') as fi:
        for y in fi:
            # only execute the first row building once
            if init:
                for x in range(len(y.strip())+1):
                    emptyRow.append(10)
                    init = False
                data.append(emptyRow)
            dataX = []
            # add leading "10"
            dataX.append(10)
            for x in y.strip():
                dataX.append(int(x))
            # add ending "10"
            dataX.append(10)
            data.append(dataX)
        data.append(emptyRow)
    return(data)

def prMatrix(matrix):
    for y in matrix:
        print(y)

def getLowPoints(matrix):
    # prMatrix(matrix)
    lowPoints = []
    lowCoordinates = []
    # exclude "10" top and bottom borders in analyzing
    for i in range(len(matrix)-1):
        # exclude "10" left and right borders in analyzing
        for j in range(len(matrix[i])-1):
            # smaller than top, bottom, left and right element
            if matrix[i][j] < matrix[i-1][j] \
               and matrix[i][j] < matrix[i+1][j] \
               and matrix[i][j] < matrix[i][j-1] \
               and matrix[i][j] < matrix[i][j+1]:
                # low point detected, save value and Coordinates
                lowPoints.append(matrix[i][j])
                lowCoordinates.append((i,j))
    return(lowPoints,lowCoordinates)

def calcSum1(points):
    total = 0
    for val in points:
        total += val + 1
    return total


def calcBasin(tu, matrix):
    # global list of already checked positions needed to avoid endless loop
    global checkedPos
    # store coordinates in variables for easier use
    y = tu[0]
    x = tu[1]
    # calculate coordinates of adjacent fields
    top = (y+1,x)
    right = (y,x+1)
    left = (y,x-1)
    bot = (y-1,x)
    # store adjacent fields in list
    dirIDs = [top,right,bot,left]
    if matrix[y][x] < 9:
        # part of the basin detected
        # store this field in global list of already checked fields
        checkedPos.append(tu)
        # found field so count is "1"
        val = 1
        for i in dirIDs:
            if i not in checkedPos:
                # increase count by every not already checked adjacent field
                val += calcBasin(i, matrix)
    else:
        # border detected
        val = 0
    return val


def getBasin(lowCoords, matrix):
    basin = []
    # run through all the earlier found coordinates (saved as tuples)
    for t in lowCoords:
        # initialize counter variable
        val = 0
        # start recursive check
        val += calcBasin(t, matrix)
        # append basin size in list
        basin.append(val)
    return(basin)

def part1():
    lowPoints = getLowPoints(readInput(PUZZLE_INPUT))[0]
    print("Part1:",calcSum1(lowPoints))


def part2():
    lowCoords = getLowPoints(readInput(PUZZLE_INPUT))[1]
    basins = getBasin(lowCoords,readInput(PUZZLE_INPUT))
    basins = sorted(basins)
    totalPart2 = 1
    # multiply last 3 elements in sorted list
    for spot in basins[-3:]:
        totalPart2 *= spot
    print("Part2:",totalPart2)


if __name__ == '__main__':
    part1()
    part2()
