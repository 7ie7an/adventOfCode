TEST_INPUT = "2021/test.txt"
PUZZLE_INPUT = "2021/2021_08.txt"

def readInput(filename):
    data = []
    with open(filename, 'r') as fi:
        for li in fi:
            data.append([li.strip().split(" | ")[0].split(" "), li.strip().split(" | ")[1].split(" ")])
    return data

def identifyEasySegment(data):
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

def remDupl(string):
    newString = []
    for i in string:
        if i not in newString:
            newString.append(i)
    return "".join(newString)

def convSegmentLetters(row):
    segDis = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    zero69 = []
    two35 = []
    for el in row:
        if len(el) == 2:
            segDis[1] = "".join(sorted(el))
            # 1 found
        elif len(el) == 3:
            segDis[7] = "".join(sorted(el))
            # 7 found
        elif len(el) == 4:
            segDis[4] = "".join(sorted(el))
            # 4 found
        elif len(el) == 7:
            segDis[8] = "".join(sorted(el))
            # 8 found
        elif len(el) == 6:
            # 0, 6 or 9
            zero69.append(el)
        elif len(el) == 5:
            # 2, 3 or 5
            two35.append(el)

    # top bar is the one additional bar that a "7" has over a "1"
    # and is identified as "d" in the example
    for c in segDis[7]:
        if c not in segDis[1]:
            topSeg = c
    # create combination of strings to get a 9 without bottom segment
    woBot9 = remDupl(sorted(segDis[1] + segDis[7] + segDis[4]))
    for el in zero69:
        # 9 in segment is the only one of those 3
        # that has only 1 additional segment compared to 4 + 7 segment
        if len(remDupl(sorted(woBot9 + el))) == len(woBot9) +1:
            segDis[9] = "".join(sorted(el))
        # 0 is the only number of those 3
        # that combined with a 1 doesn't change
        elif remDupl(sorted(el + segDis[1])) == "".join(sorted(el)):
            segDis[0] = "".join(sorted(el))
        # 6 is the only one left over with 6 segments
        else:
            segDis[6] = "".join(sorted(el))
    for el in two35:
        # 5 is the only number of those 3
        # that only differs in 1 segment to 6
        if len(remDupl(sorted(el+segDis[6]))) - 1 == len(el):
            segDis[5] = "".join(sorted(el))
        # 3 is the only number of those 3
        # that combined with a 1 doesn't change
        elif remDupl(sorted(el + segDis[1])) == "".join(sorted(el)):
            segDis[3] = "".join(sorted(el))
        # 2 is the only one left over with 5 segments
        else:
            segDis[2] = "".join(sorted(el))
    return(segDis)

def identifySegment(data):
    val = 0
    for j in data:
        pat = convSegmentLetters(j[0])
        cat = ""
        for el in j[1]:
            # index the element string with the segmented list
            cat += str(pat.index("".join(sorted(el))))
        val += int(cat)
    return val


def part1():
    print("Part1:", identifyEasySegment(readInput(PUZZLE_INPUT)))

def part2():
    print("Part2:", identifySegment(readInput(PUZZLE_INPUT)))

if __name__ == '__main__':
    part1()
    part2()
