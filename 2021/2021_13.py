TEST_INPUT = "2021/test_13.txt"
PUZZLE_INPUT = "2021/2021_13.txt"

class Transparent:
    block = []
    foldInstructions = []
    inpFile = ""
    def __init__(self):
        pass

    def readInput(self,filename):
        with open(filename, 'r') as fi:
            inBlock = True
            block = []
            foldings = []
            for li in fi:
                if li == "\n":
                    inBlock = False
                # Flag to identify if we are still in dot/mark block
                elif inBlock:
                    # first y second x coordinate to improve console printing
                    block.append((int(li.strip().split(",")[1]), int(li.strip().split(",")[0])))
                # Folding instructions
                else:
                    # (dir,val)
                    foldings.append((li.strip().split("=")[0][-1:],int(li.strip().split("=")[1])))
            self.block =  block
            self.foldInstructions = foldings

    def printBlock(self, empty):
        maxX = 0
        maxY = 0
        pBlock = []
        # get block size
        for y,x in self.block:
            if y > maxY:
                maxY = y
            if x > maxX:
                maxX = x
        for j in range(maxY +1):
            tmpBlock = []
            for i in range(maxX +1):
                if (j,i) in self.block:
                    tmpBlock.append("#")
                else:
                    tmpBlock.append(empty)
            pBlock.append(tmpBlock)
        for line in pBlock:
            print("".join(line))

    def fold(self,index):
        fold = self.foldInstructions[index]
        for i in range(len(self.block)):
            y = self.block[i][0]
            x = self.block[i][1]
            if fold[0] == "y" and y > fold[1]:
                self.block[i] = (fold[1]-(y-fold[1]),x)
            elif fold[0] == "x" and x > fold[1]:
                self.block[i] = (y,fold[1]-(x-fold[1]))

    def countDots(self):
        dots = []
        for dot in self.block:
            if dot not in dots:
                dots.append(dot)
        print(len(dots))

def part1():
    p1 = Transparent()
    p1.readInput(PUZZLE_INPUT)
    print("\n=====FOLD1=====")
    p1.fold(0)
    # p1.printBlock(" ")
    p1.countDots()


def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()
