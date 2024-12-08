safe_reports = 0
removed = False
difference_per_level = []

def strictlyascending(list):
    return all(list[index] < list[index + 1] for index in range(0,len(list) - 1))

def strictlydescending(list):
    return all(list[index] > list[index + 1] for index in range(0,len(list) - 1))

input_file=open("input.txt","r")

for report_list in input_file:
    report=report_list.rstrip('\n').split(" ")
    report = list(map(int, report))
    x = 0
    difference_per_level.clear()
    while removed == False or x in range(0,len(report)):
        if strictlyascending(report) or strictlydescending(report):
            for y in range(0,len(report) - 1):
                difference = abs(report[y] - report[y + 1])
                difference_per_level.append(difference)
            difference_per_level.sort(reverse=True)
            if difference_per_level[0] <= 3:
                safe_reports += 1
                removed = True
                x = len(report) + 1
            else: x += 1
        elif x in range(0,len(report)):
            buffer = report[x]
            report.pop(x)
            removed = True
            if strictlyascending(report) or strictlydescending(report):
                for y in range(0,len(report) - 1):
                    difference = abs(report[y] - report[y + 1])
                    difference_per_level.append(difference)
                difference_per_level.sort(reverse=True)
                if difference_per_level[0] <= 3:
                    safe_reports += 1
                    removed = True
                    x = len(report) + 1
            else:
                report.insert(x,buffer)
                x += 1
                removed = False
        else: 
            x = len(report) +1
            removed = True
print ("Part 2: Anzahl sicherer Reports mit Dampener:",safe_reports)