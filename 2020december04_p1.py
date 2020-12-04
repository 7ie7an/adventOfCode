import os

input_file = "2020december_passports.txt"

passports_raw = []
passports_in_strings = []
passports = [{}]
passports_counter = 0

# extract passport data per person as a single string
with open(input_file, 'r') as file:
    buffer_var = ""
    for line in file:
        passports_raw.append(line)
    passports_raw.append("\n")

for row in range(len(passports_raw)):
    # new line is used to separate passports
    if passports_raw[row] == "\n" or passports_raw[row] == "\n":
        passports_in_strings.append(buffer_var)
        buffer_var = ""
    else:
        # data between two empty new lines (passports)
        # can also contain a newline character @the end of the line
        buffer_var += passports_raw[row].replace("\n"," ")

for string in passports_in_strings:
    passports.append({})
    # whitespaces separate keys
    fields = string.split()
    for properties in fields:
        properties = properties.split(":")
        passports[passports_counter].update({properties[0]:properties[1]})
    passports_counter += 1

#remove last empty element
passports.pop()

#debug variables
members = 0
invalid = 0
valid_passports = 0

#detect if anything is missing
for entry in passports:
    members += 1
    if (("byr" not in entry) or
        ("iyr" not in entry) or
        ("eyr" not in entry) or
        ("hgt" not in entry) or
        ("hcl" not in entry) or
        ("ecl" not in entry) or
        ("pid" not in entry)):
        invalid += 1
    else:
        valid_passports += 1

print(f'Members:{members}\nValid Passports:{valid_passports}\nInvalid Passports:{invalid}')
