import math

PUZZLE_INPUT = "2021/2021_07.txt"
TEST_INPUT = "2021/test.txt"

def readInput(filename):
    crabPositions = []
    with open(filename, 'r') as fi:
        crabPositions = fi.readline().split(",")
        for i in range(len(crabPositions)):
            crabPositions[i] = int(crabPositions[i])
    return crabPositions

def calcMedian(li):
    median = 0
    if len(li)%2 == 0:
        median = li[int(len(li)/2)]
    else:
        median = int((li[math.floor(len(li)/2)] + li[math.ceil(len(li)/2)])/2)
    return median

def calcMean(li):
    mean = 0
    for var in li:
        mean += var
    mean = int(mean/len(li))
    return mean

def calcFuellLin(li, me):
    fuelCost = 0
    for var in li:
        fuelCost += abs(var-me)
    return fuelCost

def calcFuellIncr(li, me):
    fuelCost = 0
    fuelCostGauss = 0
    # run through all crabs
    for var in li:
        n = abs(var - me)
        # https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Summenformel
        value = int(((n*(n+1))/2))
        fuelCrab = 0
        if var != me:
            # add the step size recursively
            for i in range(1,abs(var-me)+1):
                fuelCrab += abs(i)
        elif var == me:
            print("special Case")
        fuelCostGauss += value
        fuelCost += fuelCrab
    print("Part2 Gauss Solution:", fuelCostGauss)
    return fuelCost

def part1():
    pos = readInput(PUZZLE_INPUT)
    pos.sort()
    med = calcMedian(pos)
    print("Part1 Solution:",calcFuellLin(pos,med))

def part2():
    pos = readInput(PUZZLE_INPUT)
    pos.sort()
    mea = calcMean(pos)
    print("Part2 Solution ", calcFuellIncr(pos,mea))

if __name__ == '__main__':
    part1()
    part2()
