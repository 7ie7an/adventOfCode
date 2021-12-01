counter = 0
first = True
meassurements = []

def getSum(mlist, index):
    sum = 0
    sum = mlist[index] + mlist[index+1] + mlist[index+2]
    return sum

with open("2021/2021_01.txt", 'r') as file:
    for line in file:
        meassurements.append(int(line))

last = getSum(meassurements, 0)
print(last, "(N/A - no previous measurement)", sep=" ")
for index in range(len(meassurements)):
    if index < (len(meassurements)-2) and index > 0:
        current = getSum(meassurements,index)
        if current > last:
            print(current, "(increased)", sep=" ", end=' ')
            counter += 1
        else:
            print(current, "(decreased)", sep=" ", end=' ')
        print(current - last)
        last = current
print("Test","sum of last 3 elements", ":",
      meassurements[len(meassurements)-3] \
      + meassurements[len(meassurements)-2] \
      + meassurements[len(meassurements)-1], sep=" ")
print("Counter:", counter, sep=" ")
