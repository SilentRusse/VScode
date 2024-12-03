list_1 = []
list_2 = []
input_file=open("input.txt","r")
for row in input_file:
    buffer=row.rstrip('\n').split("   ")
    list_1.append(buffer[0])
    list_2.append(buffer[1])
list_1.sort()
list_2.sort()
summary = 0
difference = 0
x = 0
for x in range (0,len(list_1)):
    difference = 0
    difference = int(list_1[x]) - int(list_2[x])
    if difference < 0:
        difference = int(list_2[x]) - int(list_1[x])
    summary += difference
print(summary)