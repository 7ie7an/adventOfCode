TEST_INPUT = "2021/test_11.txt"
PUZZLE_INPUT = "2021/2021_11.txt"

class BioCave:
    def __init__(self):
        self.mapS = []
        pass

    def readInput(self,filename):
        data = []
        with open(filename, 'r') as fi:
            for li in fi:
                dataX = []
                [dataX.append(x) for x in li.strip()]
                data.append(dataX)
        self.mapS = data

# Solution of Part 1
def part1():
    p1 = BioCave()
    print("Part1:")

# Solution of Part 2
def part2():
    p2 = BioCave()
    p2.readInput(TEST_INPUT)
    print("Part2:")

if __name__ == '__main__':
    part1()
    part2()
