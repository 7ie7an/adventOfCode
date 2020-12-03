import os
import re


min_pos = 0
max_pos = 1
letter_pos = 2
password_pos = 3

valid_passwords = 0

input_file = "2020december_passwords.txt"
with open(input_file, 'r') as file:
    for line in file:
        count_occ = 0
        line_ssv = line.replace("-"," ").replace(":","")
        line_ssv = line_ssv.split()
        line_ssv[min_pos] = int(line_ssv[min_pos])
        line_ssv[max_pos] = int(line_ssv[max_pos])
        for char in line_ssv[password_pos]:
            if char == line_ssv[letter_pos]:
                count_occ += 1
        if (count_occ >= line_ssv[min_pos]) and (count_occ <= line_ssv[max_pos]):
            valid_passwords += 1
print(valid_passwords)
