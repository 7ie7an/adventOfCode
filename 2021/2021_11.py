TEST_INPUT = "2021/test_11.txt"
PUZZLE_INPUT = "2021/2021_11.txt"

class BioCave:
    def __init__(self):
        self.mapS = []
        self.flashed = []
        self.flashCount = 0
        pass

    def readInput(self,filename):
        data = []
        with open(filename, 'r') as fi:
            for li in fi:
                dataX = []
                [dataX.append(int(x)) for x in li.strip()]
                data.append(dataX)
        self.mapS = data

    def createBorder(self):
        empty = []
        data = []
        for i in range(len(self.mapS[0])+2):
            empty.append(11)
        data.append(empty)
        for y in self.mapS:
            tmp = []
            tmp.append(11)
            for x in y:
                tmp.append(x)
            tmp.append(11)
            data.append(tmp)
        data.append(empty)
        self.mapS = data

    def printMap(self):
        for y in self.mapS:
            print(y)

    def __flash(self,y,x):
        positions = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
        # run through all adjacent positions
        for tu in positions:
            # increase due to neighbor flash
            if self.mapS[tu[0]][tu[1]] < 10:
                self.mapS[tu[0]][tu[1]] += 1
            # execute flash because new flash detected
            if self.mapS[tu[0]][tu[1]] == 10 and (tu[0],tu[1]) not in self.flashed:
                self.flashed.append((tu[0],tu[1]))
                self.__flash(tu[0],tu[1])
            else:
                pass

    def __checkFlash(self,y,x):
        if self.mapS[y][x] == 10 and (y,x) not in self.flashed:
            self.flashed.append((y,x))
            self.__flash(y,x)

    def executeStep(self):
        # step 1 - increase
        for iy in range(1,len(self.mapS)-1):
            for ix in range(1,len(self.mapS[1])-1):
                self.mapS[iy][ix] +=1
        # self.printMap()
        # step 2 - recursively flash
        for iy in range(1,len(self.mapS)-1):
            for ix in range(1,len(self.mapS[1])-1):
                self.__checkFlash(iy,ix)
        # self.printMap()
        self.flashCount += len(self.flashed)
        self.flashed.clear()
        # step 3 - reset
        for iy in range(1,len(self.mapS)-1):
            for ix in range(1,len(self.mapS[1])-1):
                if self.mapS[iy][ix] == 10:
                    self.mapS[iy][ix] = 0
        # self.printMap()

    def checkAllFlashed(self):
        zeroCount = 0
        for iy in range(1,len(self.mapS)-1):
            for ix in range(1,len(self.mapS[1])-1):
                if self.mapS[iy][ix] == 0:
                    zeroCount += 1
        if zeroCount == ((len(self.mapS)-2)*(len(self.mapS)-2)):
            return False
        else:
            return True

# Solution of Part 1
def part1():
    p1 = BioCave()
    p1.readInput(PUZZLE_INPUT)
    p1.createBorder()
    for i in range(100):
        p1.executeStep()
    p1.printMap()
    print("Part1:", p1.flashCount)

# Solution of Part 2
def part2():
    p2 = BioCave()
    p2.readInput(PUZZLE_INPUT)
    p2.createBorder()
    index = 0
    while p2.checkAllFlashed():
        p2.executeStep()
        index += 1
    p2.printMap()
    print("Part2:", index)

if __name__ == '__main__':
    part1()
    part2()
