"""This module solves the first part of Advent-of-Code 2020 December 7th."""
# --- Day 7: Handy Haversacks ---

# You land at the regional airport in time for your next flight. In fact, it looks like you'll even
# have time to grab some food: all flights are currently delayed due to issues in luggage processing

# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags
# and their contents; bags must be color-coded and must contain specific quantities of other
# color-coded bags. Apparently, nobody responsible for these regulations considered how long they
# would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

# These rules specify the required contents for 9 bag types. In this example, every faded blue bag
# is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different
# bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually,
# contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

#   - A bright white bag, which can hold your shiny gold bag directly.
#   - A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
#   - A dark orange bag, which can hold bright white and muted yellow bags, either of which could
#     then hold your shiny gold bag.
#   - A light red bag, which can hold bright white and muted yellow bags, either of which could
#     then hold your shiny gold bag.

# So, in this example, the number of bag colors that can eventually contain at least one shiny
# gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is
# quite long; make sure you get all of it.)
amount_of_bags = 1
function_calls = 0
bags_in_key = 0

def count_bags(key_string, bags_opened):
    global amount_of_bags
    global function_calls
    function_calls += 1
    for list_element in rules[key_string]:
        bags_in_key += list_element[1]
        if list_element[0] != "other":
            amount_of_bags *= list_element[1]

INPUT_FILE = "input_temp.txt"
raw_data = []
rules= {}

with open(INPUT_FILE, 'r') as file:
    for line in file:
        raw_data.append(line)
for rule in raw_data:
    # name of bag without whitspace between bags and last color
    bag_name = rule[:rule.find("bags")-1]
    # elements for all rules removing '.' add the end of the string
    rule_element = rule[rule.find("contain") + 8: -2]
    # remove singular and plural verions of bag because obsolete
    rule_element = rule_element.replace(" bags", "")
    rule_element = rule_element.replace(" bag", "")
    bag_spec = rule_element.split(",")
    for requirement in range(len(bag_spec)):
        bag_spec[requirement] = content = bag_spec[requirement].strip()
    bag_tspec = []
    for element in bag_spec:
        if element[0:(element.find(" "))] == "no":
            bag_tspec.append(
                (element[element.find(" ")+1:],
                 0))
        else:
            bag_tspec.append(
                (element[element.find(" ")+1:],
                 int(element[0:(element.find(" "))])))
    rules.update({bag_name:bag_tspec})
    # print(f'{bag_name}\n{bag_tspec}\n')
can_store_shiny_gold = []
can_store_shiny_gold.append("shiny gold")

recursion = 1
appeareances = 0
another_try = True
while another_try == True:
    another_try = False
    for element in rules:
        for bigger in can_store_shiny_gold:
            for tuple_element in rules[element]:
                if tuple_element[0] == bigger:
                    if element not in can_store_shiny_gold:
                        can_store_shiny_gold.append(element)
                        # stop loop if there is no new element current run
                        another_try = True
                        appeareances += 1
    recursion += 1
print(f'Possible containers:{appeareances} - Recursions needed:{recursion}')

count_bags("shiny gold")
print(function_calls, amount_of_bags)
