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
    biggest_delta = max(difference_per_level)
    if biggest_delta in range(1,3) or biggest_delta in range(-1,-3):
        safe_reports =+ 1
print(safe_reports)