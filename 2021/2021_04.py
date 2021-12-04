def readInput():
    with open("2021/2021_04.txt", 'r') as fi:
        bingoNumbers = []
        bingoBlocks = []
        row = 0
        inBlock = True
        tempRow = []
        tempBlock = []
        for li in fi:
            # cover double white space in case of one digit number
            li = li.replace("  ", " ")
            # ignore bingo number row
            if row > 0:
                # process data row
                if li[0] != "" and li[0] != "\n":
                    inBlock = True
                    # convert and add row as list object
                    tempRow.append(li.strip().split(" "))
                # new block detected
                else:
                    inBlock = False
                    # append bingo block
                    tempBlock.append(tempRow)
                    tempRow = []
            #first line contains the bingo numbers
            else:
                bingoNumbers = li.strip().split(",")
            row += 1
        # remove first empty block object
        tempBlock.pop(0)
        return tempBlock, bingoNumbers

def crossBlock(block, val):
    for r in range(len(block)):
        for c in range(len(block[0])):
            if block[r][c] == val:
                # cross a called value
                block[r][c] = block[r][c] + "_X"
    return block

def checkBlock(block):
    bingo = False
    # run through rows
    for r in block:
        counter = 0
        for val in r:
            if "_X" in val:
                # increase counter if checkmarked
                counter += 1
        if counter == len(block[0]):
            bingo = True
    counter = 0
    # run through columns
    for c in range(len(block[0])):
        # run through rows
        counter = 0
        for r in block:
            if "_X" in r[c]:
                # increase counter if checkmarked
                counter += 1
        if counter == len(block[0]):
            bingo = True
    counter = 0
    return bingo

def calcSum(val, block):
    result = 0
    for r in block:
        for c in r:
            if "_X" not in c:
                result += int(c)
    result = result * int(val)
    print("Result:", result)
    return result

def part1():
    blockList = readInput()[0]
    bingoNumbers = readInput()[1]
    bingo = False
    # check inputs one after another
    for val in bingoNumbers:
        for blockId in range(len(blockList)):
            # only do further crossing and checking if bingo wasn't found already
            if not bingo:
                # cross block and update blocklist
                blockList[blockId] = crossBlock(blockList[blockId], val)
                bingo = checkBlock(blockList[blockId])
                # stop execution as soon as bingo was found
                if bingo:
                    result = calcSum(val,blockList[blockId])

if __name__ == '__main__':
    part1()
