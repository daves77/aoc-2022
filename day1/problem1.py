data = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        data.append(line)

max = curr_cals = 0
for el in data:
    if el == "": 
        max = curr_cals if curr_cals > max else max
        curr_cals = 0
    else:
        curr_cals += int(el)

print(max)

