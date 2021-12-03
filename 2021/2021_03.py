def readInputFile():
    input = []
    # store input data
    with open("2021/2021_03.txt", 'r') as file:
        for line in file:
            line = line.strip()
            input.append(list(line))
    return input

def calcBitCorrelation(dataList):
    correlation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # calculate correlation
    for element in dataList:
        for x in range(len(element)):
            if int(element[x]) == 1:
                correlation[x] += 1
            elif int(element[x]) == 0:
                correlation[x] -= 1
            else:
                print("error")
    #print("0 and 1 Correlation:", correlation, sep=" ")
    return correlation

def calcSolution(bitCor):
    gamma = 0
    epsilon = 0
    # convert absolut value
    for counter in range(len(bitCor)):
        if bitCor[counter] > 0:
            gamma |= 1
            epsilon |=0
        elif bitCor[counter] < 0:
            gamma |= 0
            epsilon |=1
        else:
            print("error")
        gamma = gamma << 1
        epsilon = epsilon <<1
    # Backshift the last loop shift
    gamma = gamma >> 1
    epsilon = epsilon >>1
    print("Binary ", bin(gamma),   "| Decimal ", gamma,    sep=" - ")
    print("Binary ", bin(epsilon), "| Decimal ", epsilon,  sep=" - ")
    return(gamma*epsilon)

def getUnifiedBitCorrelation(dataList):
    cor = calcBitCorrelation(dataList)
    oxyList = []
    co2List = []
    for element in cor:
        if element > 0:
            oxyList.append(1)
            co2List.append(0)
        elif element < 0:
            oxyList.append(0)
            co2List.append(1)
        else:
            oxyList.append(1)
            co2List.append(0)
    return oxyList, co2List

def convertListToBin(dataList):
    binList = []
    for element in dataList[0]:
        binList.append(int(element))
    return binList

def getFilteredList(dataList, position, corBit):
    filteredList = []
    for element in dataList:
        # only save elements where value bit equals desired correlation bit
        if int(element[position]) == corBit:
            filteredList.append(element)
    return filteredList

def part2(dataList):
    # starting point of both calculation is the same
    oxygenList = dataList.copy()
    co2List = dataList.copy()
    # amount of bits to be checked
    for counter in range(len(dataList[0])):
        # recalculate correlations
        corOxy = getUnifiedBitCorrelation(oxygenList)[0]
        corC02 = getUnifiedBitCorrelation(co2List)[1]
        # ignore processing if last element already found
        if len(oxygenList) > 1:
            # filter for correlated lists
            oxygenList = getFilteredList(oxygenList,counter,corOxy[counter])
        # ignore processing if last element already found
        if len(co2List) > 1:
            # filter for correlated lists
            co2List = getFilteredList(co2List,counter,corC02[counter])
    print("\n==PART 2==")
    print("Binary ", bin(int("".join(oxygenList[0]),2)), "| Decimal ", int("".join(oxygenList[0]),2) , sep=" - ")
    print("Binary ", bin(int("".join(co2List[0]),2)),  "| Decimal ", int("".join(co2List[0]),2), sep=" - ")
    print("Product:", int("".join(co2List[0]),2)*int("".join(oxygenList[0]),2), sep=" ")

def part1(dataList):
    print("==PART 1==")
    bitCorrelation = calcBitCorrelation(inputData)
    solution = calcSolution(bitCorrelation)
    print("Product:", solution, sep=" ")

if __name__ == '__main__':
    inputData = readInputFile()
    part1(inputData)
    part2(inputData)
