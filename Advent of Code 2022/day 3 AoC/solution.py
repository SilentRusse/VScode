from shlex import join
import string
backpack = open("day 3 AoC\data.txt").read().split("\n")
priority = 0
common_letters = []
badge = []
for compartment in backpack:
    cut = int(len(compartment)/2)
    slot_1 = compartment[:cut]
    slot_2 = compartment[cut:]
    letter = join(set(slot_1).intersection(slot_2))
    priority += int(string.ascii_letters.index(letter) + 1)
print(f"Summe aller Prioritaeten:{priority}")
priority = 0
for compartment in backpack:
    badge.append(compartment)
    if len(badge) >= 3:
        for letter in badge[0]:
            if letter in badge[1] and letter in badge[2]:
                priority += string.ascii_letters.index(letter) + 1
                badge = []
                break
print(f"Sum of Priority Badges: {priority}")