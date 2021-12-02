counter = 0
forward = 0
level = 0
with open("2021/2021_02.txt", 'r') as file:
    for line in file:
        instructions = line.split()
        if instructions[0] == "forward":
            forward += int(instructions[1])
        elif instructions[0] == "down":
            level += int(instructions[1])
        elif instructions[0] == "up":
            level -= int(instructions[1])
        else:
            print("error")
    print(level*forward)
