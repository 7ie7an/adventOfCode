TEST_INPUT = "2021/test.txt"
PUZZLE_INPUT = "2021/2021_10.txt"
closing = [")", ">", "]", "}"]
opening = ["(", "<", "[", "{"]

def readInput(filename):
    data = []
    with open(filename, 'r') as fi:
        for li in fi:
            row = []
            for c in li.strip():
                row.append(c)
            data.append(row)
    return data

def findCorrupt(data):
    # save row index
    index = 0
    corrupts = []
    for row in data:
        length = len(row)
        i = 0
        while (i < length):
            # check if closing parantheses
            if row[i] in closing:
                # is the para before the exact same opening parantheses
                if row[i-1] == opening[closing.index(row[i])]:
                    # remove para pair from data because valid
                    row.pop(i)
                    row.pop(i-1)
                    # restart loop
                    i = 0
                    length -= 2
                else:
                    # this para does not fit the the row
                    corrupts.append((index,row[i]))
                    break
            elif row[i] not in opening:
                # mismatch in programm
                print("error")
            # increase loop counter
            i += 1
        index += 1
    return (corrupts)

def calcSum1(corrupts):
    sum1 = 0
    for tu in corrupts:
        if tu[1] == ")":
            sum1 += 3
        elif tu[1] == "]":
            sum1 += 57
        elif tu[1] == "}":
            sum1 += 1197
        elif tu[1] == ">":
            sum1 += 25137
    return(sum1)
def completeRow(row):
    i = len(row)-1
    missing = []
    while i >= 0:
        if row[i] in opening:
            # cover the case of the last element beeing a opening para
            if i == len(row)-1:
                row.append(closing[opening.index(row[i])])
                # an opening para at the end has to be missing
                missing.append(closing[opening.index(row[i])])
                # reset loop
                i = len(row)
            # is the para before the exact same opening parantheses
            elif row[i+1] == closing[opening.index(row[i])]:
                # remove para pair from data because valid
                row.pop(i+1)
                row.pop(i)
                # restart loop
                i = len(row)
            else:
                # mismatch in programm
                print("error")
        elif row[i] not in closing:
            # mismatch in programm
            print("error")
        # decrease loop counter
        i -= 1
    return missing

def calcSum2(paraLists):
    results = []
    for li in paraLists:
        score = 0
        for c in li:
            score *= 5
            if c == ")":
                score += 1
            elif c == "]":
                score += 2
            elif c == "}":
                score += 3
            elif c == ">":
                score += 4
        results.append(score)
    results = sorted(results)
    return (results[int(len(results)/2)])

def part1():
    data = readInput(PUZZLE_INPUT)
    corrupts = findCorrupt(data)
    print("Part1:", calcSum1(corrupts))


def part2():
    data = readInput(PUZZLE_INPUT)
    corrupts = findCorrupt(data)
    ignoreLines = []
    results = []
    i = 0
    [ignoreLines.append(n) for n,c in corrupts]
    for row in data:
        if i not in ignoreLines:
            results.append(completeRow(row))
        i += 1
    total2 = calcSum2(results)
    print("Part2:", total2)
if __name__ == '__main__':
    part1()
    part2()
