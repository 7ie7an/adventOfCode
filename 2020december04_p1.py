import os

input_file = "2020december_passports.txt"
#input_file = "input_temp.txt"
persons = [{}]
person_data = []
with open(input_file, 'r') as file:
    for line in file:
        person_data.append(line)

buffer_var = ""
person_strings = []
for row in range(len(person_data)):
    if person_data[row] == "\n":
        person_strings.append(buffer_var)
        buffer_var = ""
    else:
        person_data[row] = person_data[row].replace("\n"," ")
        buffer_var += person_data[row]

ids = 0
for string in person_strings:
    persons.append({})
    fields = string.split()
    for properties in fields:
        prop = properties.split(":")
        dict_entry = {prop[0]:prop[1]}
        print(ids)
        persons[ids].update(dict_entry)
    ids += 1

#remove last empty element
persons.pop()

#debug variables
members = 0
invalid = 0
valid_passports = 0
#detect if anything is missing
for person_dict_data in persons:
    members += 1
    if ("byr" not in person_dict_data) or ("iyr" not in person_dict_data) or ("eyr" not in person_dict_data) or ("hgt" not in person_dict_data) or ("hcl" not in person_dict_data) or ("ecl" not in person_dict_data) or ("pid" not in person_dict_data):
        print("invalid")
        invalid += 1
    else:
        print("valid")
        valid_passports += 1
print(f'{person_id}:{members}:{valid_passports}:{invalid}')
