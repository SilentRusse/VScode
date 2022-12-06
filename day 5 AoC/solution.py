import re
import string
import collections
stacks = open("day 5 AoC\data.txt").read().split("\n")
instructions = []
container = []
mylist = []
row_number = []
for line in stacks:
    if 'move' in line:
        instructions.append(re.findall("[0-9]",line))
    else: 
        container.append(list(enumerate(line)))
count = 0
for item in container:
    for letter in item:
        if type(letter[0]) == int and letter[1].isalpha():
            mylist[letter[0]].append(letter[1])
        elif type(letter[0]) == int and type(letter[1]) == int:
            mylist[letter[0]].append([])