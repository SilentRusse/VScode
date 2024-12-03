list_1 = []
list_2 = []
occurance=[]
multiplied=[]

summary_part1 = 0
summary_part2 = 0
difference = 0
x = 0

input_file=open("input.txt","r")
for row in input_file:
    buffer=row.rstrip('\n').split("   ")
    list_1.append(buffer[0])
    list_2.append(buffer[1])
list_1.sort()
list_2.sort()
for x in range (0,len(list_1)):
    difference = 0
    difference = int(list_1[x]) - int(list_2[x])
    if difference < 0:
        difference = int(list_2[x]) - int(list_1[x])
    summary_part1 += difference
print(summary_part1)
# Solution Day 1 Part 1
for x in range (0,len(list_1)):
    occurance.append(list_2.count(list_1[x]))
for x in range (0,len(list_1)):
    multiplied.append(int(list_1[x]) * int(occurance[x]))
summary_part2 = sum(multiplied)
print(summary_part2)
# Solution Day 1 Part 2