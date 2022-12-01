data = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        data.append(line)

top = []
curr_cals = 0
for el in data:
    if el == "": 
        if len(top) == 3:
            lowest = min(top)
            if curr_cals > lowest:
                top.remove(lowest)
                top.append(curr_cals)
        else:
            top.append(curr_cals)
        curr_cals = 0
    else:
        curr_cals += int(el)
print(top)
print(sum(top))