
input = []
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = 0
epsilon = 0
# store input data
with open("2021/2021_03.txt", 'r') as file:
    for line in file:
        line = line.strip()
        input.append(list(line))
# calculate correlation
for element in input:
    for x in range(len(element)):
        if int(element[x]) == 1:
            result[x] += 1
        elif int(element[x]) == 0:
            result[x] -= 1
        else:
            print("error")
# convert absolut value
for counter in range(len(result)):
    if result[counter] > 0:
        gamma |= 1
        epsilon |=0
    elif result[counter] < 0:
        gamma |= 0
        epsilon |=1
    else:
        print("error")
    gamma = gamma << 1
    epsilon = epsilon <<1
# Backshift the last loop shift
gamma = gamma >> 1
epsilon = epsilon >>1
print("0 and 1 Correlation:", result, sep=" ")
print("Binary ", bin(gamma),   "| Decimal ", gamma,    sep=" - ")
print("Binary ", bin(epsilon), "| Decimal ", epsilon,  sep=" - ")
print("Product:", gamma*epsilon, sep=" ")
