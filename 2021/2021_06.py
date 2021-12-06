CHECK_DATE = 80
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

def part1():
    # lantern list , day
    lanterns = [readInput("2021/2021_06.txt"), 0]
    while lanterns[1] < CHECK_DATE:
        lanterns = nextDay(lanterns[0],lanterns[1])
    print(len(lanterns[0]), sep="\n")

if __name__ == '__main__':
          part1()
