data = open ("day 1 AoC\data.txt").read().split("\n")
wert1 = int(0)
ergebnisse = []
for calorien in data:
    if calorien == "":
        ergebnisse.append(int(wert1))
        wert1 = 0
    else: wert1 += int(calorien)
print(f"Most calories: {max(ergebnisse)}")
ergebnisse.sort(reverse=True)
top_three = ergebnisse[0] + ergebnisse[1] +ergebnisse[2]
print(f"Top three total calories: {top_three}")
