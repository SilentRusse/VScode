from tracemalloc import start


data = open("day 4 AoC\data.txt").read().split("\n")
count = 0
for section in data:
    part1 , part2 = section.split(",")
    smallest , biggest = part1.split("-")
    start_range , end_range = part2.split("-")
    smallest = int(smallest)
    biggest = int(biggest)
    start_range = int(start_range)
    end_range = int(end_range)
    if smallest in range(start_range, end_range+1) and biggest in range(start_range, end_range+1):
        count += 1
    elif smallest == start_range and biggest == end_range:
        count += 1
    elif start_range in range(smallest, biggest +1) and end_range in range(smallest, biggest +1):
        count += 1
print(f"number of intersections: {count}")
count = 0
for section in data:
    part1 , part2 = section.split(",")
    smallest , biggest = part1.split("-")
    start_range , end_range = part2.split("-")
    smallest = int(smallest)
    biggest = int(biggest)
    start_range = int(start_range)
    end_range = int(end_range)
    range_1 = range(smallest,biggest+1)
    range_2 = range(start_range,end_range+1)
    if set(range_1).intersection(range_2):
        count += 1
print(f"total number of overlaps: {count}")