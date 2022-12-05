import re
import string
stacks = open("day 5 AoC\data.txt").read().split("\n")
container = []
stack_number = []
instructions = []
index_number = []
for line in stacks:
    if string.ascii_uppercase in line:
        container.append()
    print(container)
    if "move" in line:
        instructions.append(find_number)
    else:
        stack_number.append(find_number)