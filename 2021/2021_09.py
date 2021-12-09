TEST_INPUT = "2021/test.txt"
PUZZLE_INPUT = "2021/2021_09.txt"

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
    # exclude "10" top and bottom borders in analyzing
    for i in range(len(matrix)-1):
        # exclude "10" left and right borders in analyzing
        for j in range(len(matrix[i])-1):
            # smaller than top, bottom, left and right element
            if matrix[i][j] < matrix[i-1][j] \
               and matrix[i][j] < matrix[i+1][j] \
               and matrix[i][j] < matrix[i][j-1] \
               and matrix[i][j] < matrix[i][j+1]:
                lowPoints.append(matrix[i][j])
    return(lowPoints)

def calcSum1(points):
    total = 0
    for val in points:
        total += val + 1
    return total

def part1():
    lowPoints = getLowPoints(readInput(PUZZLE_INPUT))
    print("Part1:",calcSum1(lowPoints))
    pass

def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()
