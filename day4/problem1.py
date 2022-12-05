import pathlib
import string

cwd = pathlib.Path(__file__).parent.resolve()

with open(f'{cwd}/input.txt', 'r') as f:
    data = f.read().splitlines()

split_dash = lambda x: x.split('-')

formatted = []
for el in data:
    split = el.split(",")
    formatted.append(list(map(split_dash, split)))

def contains_pair(pair1, pair2):
    # god damn got an error because i didnt change the type. was doing string comparison vs int
    if int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]):
        return True
    return False

count = 0

for el in formatted:
    pair1 = el[0]
    pair2 = el[1]
    if contains_pair(pair1, pair2) or contains_pair(pair2, pair1):
        print(pair1, pair2)
        count += 1

print(count)
