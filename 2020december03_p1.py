import os

# Data Array
map = [[]]

# Fill map with 2d data
with open("2020december_puzzle.txt", 'r') as file:
    row=0
    for line in file:
        line.rstrip('\n')
        map.append([])
        column = 0
        for element in line:
            column += 1
            if element != "\n":
                map[row].append(element)
        print(f'Row{row+1}: {map[row]}')
        row += 1

x_pos=1
y_pos=0
x_steps = 3
y_steps = 1

tree_collide = 0
# list of y and x value
player_pos = [0,0]
for row in range (len(map)):
    for element in range(len(map[row])):
        if (player_pos[x_pos] == element) and (player_pos[y_pos] == row):
            if map[row][element] == ".":
                print(f'Pos X(element):Y(row) {player_pos[x_pos]}:{player_pos[y_pos]} = O')
            elif map[row][element] == "#":
                print(f'Pos X(element):Y(row) {player_pos[x_pos]}:{player_pos[y_pos]} = X')
                tree_collide += 1
            else:
                print("error")
    if(len(map[row]) > 0):
        player_pos[x_pos] += x_steps
        player_pos[x_pos] %= len(map[row])
        player_pos[y_pos] += y_steps
print(tree_collide)
