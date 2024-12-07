difference_per_level=[]
safe_reports = 0

def strictlyascending(list):
    return all(list[index] < list[index + 1] for index in range(0,len(list) - 1))

def strictlydescending(list):
    return all(list[index] > list[index + 1] for index in range(0,len(list) - 1))

input_file=open("input.txt","r")
for report_list in input_file:
    report=report_list.rstrip('\n').split(" ")
    report = list(map(int, report))
    if strictlyascending(report) or strictlydescending(report):
        for x in range(0,len(report) - 1):
            difference = abs(report[x] - report[x + 1])
            difference_per_level.append(difference)
        difference_per_level.sort(reverse=True)
        if difference_per_level[0] <= 3:
            safe_reports += 1
    difference_per_level.clear()
print("Part 1: Anzahl von sicheren Reports:",safe_reports)
#Part 1 more or less complete  . . .for unkown reasons the count of safe reports is 10% short of my answer
