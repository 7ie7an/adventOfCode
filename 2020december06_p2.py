import os

input_file = "2020december_forms.txt"
forms_raw = []
group_forms = []
group_total_tests = []
with open(input_file, 'r') as file:
    gr_buffer = ""
    for line in file:
        # group finished
        if line == "\n":
            group_forms.append(gr_buffer)
            gr_buffer = ""
        else:
            string_list = sorted(line)
            line = "".join(string_list)
            gr_buffer += line.replace("\n", " ")
    # EOF has no new line
    group_forms.append(gr_buffer)


tests_in_common = []
for string in group_forms:
    # whitespace @beginning of the line counts as well
    members = string.count(" ")
    common_buffer = 0
    different_tests = ""
    for char in string:
        if char != " " and char not in different_tests:
            different_tests += char
            if string.count(char) == members:
                common_buffer += 1
    tests_in_common.append(common_buffer)

answer_p2 = 0
for group in tests_in_common:
    answer_p2 += group
print(answer_p2)
