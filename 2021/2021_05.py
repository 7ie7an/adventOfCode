def readInput():
    with open("2021/2021_05.txt", 'r') as fi:
        data = []
        for li in fi:
            row = li.strip().split(" -> ")
            rTuple = []
            for pos in row:
                rTuple.append(tuple(pos.split(",")))
            data.append(rTuple)
    return data

def getMatrix(data):
    m = 0
    matrix = []
    for row in data:
        for tu in row:
            for val in tu:
                if m < int(val):
                    m = int(val)
    m += 1
    for x in range(m):
        column = []
        for y in range(m):
            column.append(0)
        matrix.append(column)
    return matrix

def addPath(tup, matrix):
    #start point
    x1 = int(tup[0][0])
    y1 = int(tup[0][1])
    x2 = int(tup[1][0])
    y2 = int(tup[1][1])
    diffX =  x2 - x1
    diffY =  y2 - y1
    if diffX > 0:
        stepX = 1
    else:
        stepX = -1
    if diffY > 0:
        stepY = 1
    else:
        stepY = -1
    # only horizontal or vertical paths allowed
    counter = 0
    if diffX != 0 and diffY == 0 :
        for i in range(x1,x2+stepX,stepX):
            # increase postion value from tuple start til end position
            matrix[y1][x1+counter] += 1
            counter += stepX

    elif diffY != 0 and diffX == 0 :
        for i in range(y1,y2+stepY,stepY):
            # increase position value from tuple start til end position
            matrix[y1+counter][x1] += 1
            counter += stepY
    elif diffY != 0 and diffX != 0:
        vector = [stepY,stepX]
        for i in range(abs(diffX)+1):
            matrix[y1+i*stepY][x1+i*stepX] += 1
    else:
        print("error:", diffX, diffY)
    return matrix

def fillMatrix(matrix):
    for path in readInput():
        # recursively update matrix
        matrix = addPath(path, matrix)
    return matrix

def calcSum(matrix):
    counter = 0
    for row in matrix:
        for c in row:
            if c > 1:
                counter += 1
    return counter

def part2():
    matrix = getMatrix(readInput())
    matrix = fillMatrix(matrix)
    print(calcSum(matrix))

if __name__ == '__main__':
    part2()
