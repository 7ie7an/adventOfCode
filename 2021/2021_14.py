TEST_INPUT = "2021/test_14.txt"
PUZZLE_INPUT = "2021/2021_14.txt"

class Poly:

    def __init__(self):
        self.diff = 0
        # Part 1
        self.template = ""
        self.patInsertion = []
        # Part 2
        self.templatesList = []
        self.templatesCounts = []
        self.patSplits = []



    def readInput(self,filename):
        with open(filename, 'r') as fi:
            inTemplate = True
            for li in fi:
                # first line is template
                if inTemplate:
                    self.template = li.strip()
                    for i in range(len(li.strip())-1):
                        # add patterns with appearance count of 1 because in start string
                        self.templatesList.append(li.strip()[i] + li.strip()[i+1])
                        self.templatesCounts.append(1)
                    inTemplate = False
                # after empty line pair insertion block starts
                elif li != "\n":
                    tmp = li.strip().split(" -> ")[0]
                    tmpC = li.strip().split(" -> ")[1]
                    # (template, additional char, combined)
                    self.patInsertion.append((tmp,tmpC,tmp[0]+tmpC+tmp[1]))
                    # [patIn ,(patOut1, patOut2) ]
                    self.patSplits.append([tmp,(tmp[0]+tmpC,tmpC+tmp[1])])
                    if (tmp,1) not in self.templatesList:
                        # add patterns with appearance count of 0 because not in start string
                        self.templatesList.append(tmp)
                        self.templatesCounts.append(0)

    def pairInsert(self):
        newTemplate = self.template[0]
        for i in range(len(self.template)-1):
            for t,ch,co in self.patInsertion:
                if (self.template[i] + self.template[i+1]) == t:
                    newTemplate += co[1:]
        self.template = newTemplate

    def countDiff(self):
        # B,C,H,N
        counts = [0,0,0,0]
        for c in self.template:
            if c == "B":
                counts[0] += 1
            elif c == "C":
                counts[1] += 1
            elif c == "H":
                counts[2] += 1
            elif c == "N":
                counts[3] += 1
        mi = counts[0]
        ma = 0
        for val in counts:
            if val > ma:
                ma = val
            if val < mi:
                mi = val
        self.diff = ma - mi

    def polyMorph(self):
        tmpCountList = self.templatesCounts.copy()
        # count templates that have to be morphed
        totalOld = 0
        for val in self.templatesCounts:
            totalOld += val
        index = 0
        while totalOld > 0:
            if self.templatesCounts[index] > 0:
                self.templatesCounts[index] -=1
                tmpCountList[index] -= 1
                totalOld -= 1
                # get morph pattern indexes
                for pat in self.patSplits:
                    if pat[0] == self.templatesList[index]:
                        i1 = self.templatesList.index(pat[1][0])
                        i2 = self.templatesList.index(pat[1][1])
                        break
                # increase morphed patterns
                tmpCountList[i1] += 1
                tmpCountList[i2] += 1
            # increase index
            index += 1
            # reset index if overflow
            if index > len(self.templatesCounts)-1:
                index = 0
        self.templatesCounts = tmpCountList.copy()

# Solution of Part 1
def part1():
    p1 = Poly()
    p1.readInput(TEST_INPUT)
    for i in range(10):
        p1.pairInsert()
    p1.countDiff()
    print("Part1:", p1.diff)

# Solution of Part 2
def part2():
    p2 = Poly()
    p2.readInput(TEST_INPUT)
    print(p2.patSplits)
    print(p2.templatesList)
    for i in range(1):
        p2.polyMorph()
    print("Part2:",p2.templatesCounts)

if __name__ == '__main__':
    part1()
    # part2()
