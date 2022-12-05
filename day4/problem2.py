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

count = 0
for el in formatted:
    pair1 = set([*range(int(el[0][0]), int(el[0][1])+1)])
    pair2 =  set([*range(int(el[1][0]), int(el[1][1])+1)])
    print(pair1)
    print(pair2)
    if len((pair1 & pair2)):
        count += 1

print(count)


