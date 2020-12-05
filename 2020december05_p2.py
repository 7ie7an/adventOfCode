import os

input_file = "2020december_seats.txt"
boardings = []
row_code = []
column_code = []
seatID = []
TOTAL_ROW_CHARS = 6
TOTAL_COLUMN_CHARS = 2

with open(input_file, 'r') as file:
    for line in file:
        boardings.append(line.replace("\n",""))

# calculate rows
for element in boardings:
    char_position = 0
    bitstream = 0b0
    # loop through row chars (0-6)
    for char in element[:7]:
        if char == "F":
            bitstream |= 0 << (TOTAL_ROW_CHARS - char_position)
        elif char == "B":
            bitstream |= 1 << (TOTAL_ROW_CHARS - char_position)
        else:
           print("Error")
        #print(f'{char}{char_position}:{bin(bitstream)}')
        # Diplay bit to inherite same print lenght
        bitstream |= 1 << (TOTAL_ROW_CHARS + 1)
        char_position += 1
    row_code.append(bitstream)

for element in boardings:
    char_position = 0
    bitstream = 0b0
    # loop through column chars (7-9)
    for char in element[7:]:
        if char == "L":
            bitstream |= 0 << (TOTAL_COLUMN_CHARS - char_position)
        elif char == "R":
            bitstream |= 1 << (TOTAL_COLUMN_CHARS - char_position)
        else:
           print("Error")
        bitstream |= 1 << (TOTAL_COLUMN_CHARS + 1)
        char_position += 1
    column_code.append(bitstream)

maxValue = 0
for row in range(len(boardings)):
    bufferValue = (row_code[row] & 0b1111111) * 8 + (column_code[row] & 0b111)
    seatID.append(bufferValue)
    if bufferValue > maxValue:
        maxValue = bufferValue
    # debug printing
    # print(f'Boarding:  {boardings[row]}')
    # print(f'RowCode:{bin(row_code[row])}    : {row_code[row] & 0b1111111}')
    # print(f'ColumnCode:    {bin(column_code[row])} : {column_code[row] & 0b111}')
    # print(f'SeatID: {seatID[row]}\n')
print(f'Highest SeatId:{maxValue}')

seatID.sort()
counter = 0
for seat in seatID:
    bufferValue = seat
    if counter > 0:
        # compare with value before
        if bufferValue - seatID[counter-1] != 1:
            print(f'My Seat Found: {bufferValue - 1}')
    counter += 1
