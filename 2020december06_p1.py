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

for string in group_forms:
    different_tests = ""
    gr_tests_buffer = len(string) - string.count(" ")
    for char in string:
        if char != " ":
            if char not in different_tests:
                different_tests += char
                # count questions answered multiple times
                # 1 occurency only counts
                gr_tests_buffer -= (string.count(char) - 1)
    group_total_tests.append(gr_tests_buffer)

answer_p1 = 0
for group in group_total_tests:
    answer_p1 += group
print(answer_p1)
