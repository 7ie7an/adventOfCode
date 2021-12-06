CHECK_DATE_1 = 80
CHECK_DATE_2 = 256

def readInput(filename):
    inp = []
    with open(filename, 'r') as fi:
        inp = fi.readline().split(",")
    for i in range(len(inp)):
        inp[i] = int(inp[i])
    return inp

def nextDay(fishList, day):
    for i in range(len(fishList)):
        fishList[i] -= 1
        if fishList[i] == -1:
            fishList[i] = 6
            fishList.append(8)
    day += 1
    return fishList, day

def countAge(fishList):
    #       0  1  2  3  4  5  6  7  8
    ages = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for el in fishList:
        ages[el] +=1
    return ages

def part1():
    # lantern list , day
    lanterns = [readInput("2021/test.txt"), 0]
    while lanterns[1] < CHECK_DATE_1:
        lanterns = nextDay(lanterns[0],lanterns[1])
    print(len(lanterns[0]), sep="\n")

def shiftAges(ageList):
    newList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(ageList)):
        # new born lanterns equal the amount of
        # last shift zero day lanterns
        if i == 8:
            newList[i] = ageList[0]
        # 6 day olds are the sum of new born and last birth giving ones
        elif i == 6:
            newList[i] = ageList[i+1] + ageList[0]
        # rest can simply be shifted from last day to today
        else:
            newList[i] = ageList[i+1]
    return newList

def calcLantern(population):
    sumPop = 0
    for el in population:
        sumPop += el
    print(sumPop)

def part2():
    ageList = countAge(readInput("2021/2021_06.txt"))
    for i in range(CHECK_DATE_2):
        ageList = shiftAges(ageList)
    calcLantern(ageList)

if __name__ == '__main__':
          part1()
          part2()
