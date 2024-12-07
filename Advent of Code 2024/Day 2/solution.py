difference_per_level=[]
safe_reports = 0

def isIncreasing(list):
    return all(list[index] < list[index + 1] for index in range(0,len(list) - 1))

def isDecreasing(list):
    return all(list[index] > list[index + 1] for index in range(0,len(list) - 1))

input_file=open("input.txt","r")
for report_list in input_file:
    report=report_list.rstrip('\n').split(" ")
    if isDecreasing(report) or isIncreasing(report):
        for x in range(0,len(report) - 1):
            difference = abs(int(report[x]) - int(report[x + 1]))
            difference_per_level.append(difference)
        difference_per_level.sort(reverse=True)
        if difference_per_level[0] <= 3:
            safe_reports += 1
    difference_per_level.clear()
print("Anzahl von sicheren Reports:",safe_reports)