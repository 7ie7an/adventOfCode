import os

input_file = "2020december_passports.txt"

passports_raw = []
passports_in_strings = []
passports = [{}]
passports_counter = 0

hair_color_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

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

for entry in passports:
    hcl_error = ""
    members += 1
    #detect if anything is missing
    if (("byr" not in entry) or
        ("iyr" not in entry) or
        ("eyr" not in entry) or
        ("hgt" not in entry) or
        ("hcl" not in entry) or
        ("ecl" not in entry) or
        ("pid" not in entry)):
        invalid += 1
    else:
        if(int(entry["byr"]) < 1920 or int(entry["byr"]) > 2002 or
           int(entry["iyr"]) < 2010 or int(entry["iyr"]) > 2020 or
           int(entry["eyr"]) < 2020 or int(entry["eyr"]) > 2030 or
           entry["hcl"][0] != "#" or
           len(entry["pid"]) != 9):
            invalid += 1
        elif(entry["hgt"][-2:] != "cm" and entry["hgt"][-2:] != "in"):
            invalid += 1
        elif(entry["ecl"] != "amb" and
             entry["ecl"] != "blu" and
             entry["ecl"] != "brn" and
             entry["ecl"] != "gry" and
             entry["ecl"] != "grn" and
             entry["ecl"] != "hzl" and
             entry["ecl"] != "oth"):
            invalid += 1
        elif entry["hcl"][0] != "#":
            invalid += 1
        else:
            for code_char in entry["hcl"][1:]:
                if code_char not in hair_color_chars:
                    print(entry["hcl"])
                    print(code_char)
                    hcl_error = "found"
            if entry["hgt"][-2:] == "cm":
                if (int(entry["hgt"][:-2]) < 150 or
                    int(entry["hgt"][:-2]) > 193):
                    invalid += 1
                else:
                    if hcl_error == "found":
                        invalid += 1
                    else:
                        valid_passports += 1
            elif entry["hgt"][-2:] == "in":
                if (int(entry["hgt"][:-2]) < 59 or
                    int(entry["hgt"][:-2]) > 76):
                    invalid += 1
                else:
                    if hcl_error == "found":
                        invalid += 1
                    else:
                        valid_passports += 1

print(f'Members:{members}\nValid Passports:{valid_passports}\nInvalid Passports:{invalid}')
