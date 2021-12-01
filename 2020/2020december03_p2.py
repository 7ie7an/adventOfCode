import os
import copy

# Data Array
map = [[]]
# +---x--->
# |........
# y........
# |........
# V........

# Fill map with 2d data
with open("2020december_puzzle.txt", 'r') as input_file:
    row=0
    for line in input_file:
        line.rstrip('\n')
        map.append([])
        column = 0
        for element in line:
            column += 1
            if element != "\n":
                map[row].append(element)
        # print(f'Row{row+1}: {map[row]}')
        row += 1

x_pos=1
y_pos=0

x_steps = 3
y_steps = 1
x_steps_list = [1,3,5,7,1]
y_steps_list = [1,1,1,1,2]

tree_collide_buffer = []
tree_collide_total = 1
output_file_name = "2020december03_output.py"
with open(output_file_name, 'w') as output_file:
    for trial in range(len(x_steps_list)):
        output_file.write(f'Trial Number: {trial}\n{x_steps_list[trial]}:{y_steps_list[trial]}\n')
        map_buffer = copy.deepcopy(map)
        # list of y and x value
        player_pos = [0,0]
        tree_collide = 0
        for row in range (len(map)):
                for element in range(len(map[row])):
                    if (player_pos[x_pos] == element) and (player_pos[y_pos] == row):
                        if map[row][element] == ".":
                            map_buffer[row][element] = "O"
                        elif map[row][element] == "#":
                            tree_collide += 1
                            map_buffer[row][element] = "X"
                        else:
                            print(f'error: {map[row][element]}')
                output_file.write(" ".join(map_buffer[row]))
                output_file.write(f' Collisions={tree_collide}\n')
                if(len(map[row]) > 0) and (row == player_pos[y_pos]):
                    player_pos[x_pos] += x_steps_list[trial]
                    player_pos[x_pos] %= len(map[row])
                    player_pos[y_pos] += y_steps_list[trial]
                    player_pos[y_pos] %= len(map)

        tree_collide_buffer.append(tree_collide)
    print(tree_collide_buffer)
    for trial in range(len(tree_collide_buffer)):
        tree_collide_total *= tree_collide_buffer[trial]
    print(f'Answer: {tree_collide_total}')
