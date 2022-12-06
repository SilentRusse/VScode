from collections import Counter
data = open("day 6 AoC\data.txt").read()
sequence = ""
Position = 0
laenge = len(data)
unique = True
for i in range(0,laenge):
    sequence += data[i]
    if(len(sequence) <= 4):
        print(Counter(sequence))
        print("\n")
    elif len(sequence) > 4 and unique == True:
        test = sequence[len(sequence) - 4:]
        Counter(test)
        #print(test)
        #print("\n")