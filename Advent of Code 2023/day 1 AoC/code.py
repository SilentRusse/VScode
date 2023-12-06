import numbers
file = open ('Advent of Code 2023\day 1 AoC\day1.txt').read().split('\n')
calibration = []
summary = []
for line in file:
    numbers_in_line = []
    for letter in line:
        if letter.isdigit() == True:
            numbers_in_line.append(letter)
    calibration.append(numbers_in_line[0] + numbers_in_line[-1])
    del numbers_in_line
calibration = list(map(int, calibration))
print(sum(calibration))
#Part One of the Challange is done

    