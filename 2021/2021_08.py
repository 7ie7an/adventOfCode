TEST_INPUT = "2021/test.txt"
PUZZLE_INPUT = "2021/2021_08.txt"

def readInput(filename):
    data = []
    with open(filename, 'r') as fi:
        for li in fi:
            data.append([li.strip().split(" | ")[0].split(" "), li.strip().split(" | ")[1].split(" ")])
    return data

def identifySegment(data):
    counter = 0
    for j in data:
        for pat in j[1]:
            if len(pat) == 2:
                # print("1")
                counter += 1
            elif len(pat) == 3:
                # print("7")
                counter += 1
            elif len(pat) == 4:
                # print("4")
                counter += 1
            elif len(pat) == 7:
                # print("8")
                counter += 1
            else:
                # print("else")
                pass

    return counter

def part1():
    print("Part1:", identifySegment(readInput(PUZZLE_INPUT)))

def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()
