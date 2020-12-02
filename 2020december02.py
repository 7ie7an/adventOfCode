import os
values = []
with open("2020december_input.txt", 'r') as file:
    row = 0
    for line in file:
        values.append(int(line))
        row += 1

position = 0
reverse_position = 0
for value in values:
    for position in range(len(values)):
        for reverse_position in range(len(values)-1,0,-1):
            if (int(value) + values[position] + values[reverse_position]) == 2020:
                print(str(value) + "+" + str(values[position]) + "+" + str(values[reverse_position]))
                print("AdventOfCode Answer: " + str(int(value) * values[position] * values[reverse_position]))
