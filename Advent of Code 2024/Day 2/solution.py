def is_ascending(lst):
    return all(
        lst[index] <= lst[index+1]
        for index in range(len(lst) - 1)
    )
def is_descending(lst):
    return all(
        lst[index] >= lst[index+1]
        for index in range(len(lst) - 1)
    )
difference_per_level=[]
safe_reports = 0
input_file=open("input.txt","r")
for report in input_file:
    report_list= report.rstrip('\n').split(" ")
    for x in range(0,len(report_list)-1):
        level_1 = int(report_list[x])
        level_2 = int(report_list[x + 1])
        absolut_diff = level_1 - level_2
        difference_per_level.append(absolut_diff)
    if (is_ascending(difference_per_level) == True or is_descending(difference_per_level) == True) and (difference_per_level in range(1,3) or difference_per_level in range(-1,-3)):
        safe_reports =+ 1
print(safe_reports)