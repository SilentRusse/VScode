import re
import string
import collections
stacks = open("day 5 AoC\data.txt").read().split("\n")
instructions = []
container = []
mylist = [[],[],[],[],[],[],[],[]]
row_number = []
for line in stacks:
    for i in range(1,len(line),4):
        if line[i].isalpha() and 'move' not in line:
            mylist.append(str(line[i]))
        elif line[i].isnumeric() and 'move' not in line:
            mylist[i].append(int(line[i]))
        elif not line[i].isalpha():
            break
        #if type(line[i]) == int:
         #   mylist.append([line[i]])
    if 'move' in line:
        instructions.append(re.findall("[0-9]",line))
count = 0
print(mylist)
print(row_number)
"""
for item in container:
    for letter in item:
        if type(letter[0]) == int and letter[1].isalpha():
            mylist.append(letter[1])
        #elif type(letter[0]) == int and type(letter[1]) == int:
            #mylist[letter[1]].append([])
"""