counter = 0
first = True
with open("2021/2021_01.txt", 'r') as file:
    for line in file:
        if first == False:
            if int(line) > last:
                print("(increased)", end=' ')
                counter += 1
            else:
                print("(decreased)", end=' ')
            print(int(line) - last)
            last = int(line)
        else:
            print("(N/A - no previous measurement)")
            last = int(line)
            first = False
    print(counter)
