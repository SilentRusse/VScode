import re
file = open ("\Advent of Code 2023\day 1 AoC\day1.txt").read().split("\n")
allnumbers = []
summary = []
for line in file:
    allnumbers =re.findall(r'\b\d+\b', line)
    last = len(allnumbers)
    summary.append = allnumbers[0] + allnumbers[last]
sum_of_calibration = sum(summary)
print (f"the sum is:{sum_of_calibration}")