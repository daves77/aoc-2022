import pathlib
import re

cwd = pathlib.Path(__file__).parent.resolve()

with open(f'{cwd}/input1.txt', 'r') as f:
    lines = f.read().splitlines()

with open(f'{cwd}/input2.txt', 'r') as f:
    steps = f.read().splitlines()

columns = int(lines[-1][-1])
number_of_colunns = []
clean_stacks = [[] for _ in range(columns)]

for line in lines:
    index = 0
    for i in range(0, len(line), 4):
        cleaned = re.sub('[^a-zA-Z]+', '', line[i:i+4])
        if cleaned:
            clean_stacks[index].insert(0, cleaned)
        index += 1

steps = [re.findall(r'\d+', step) for step in steps]

for step in steps:
    for i in range(0, int(step[0])):
       clean_stacks[int(step[2]) - 1].append(clean_stacks[int(step[1]) - 1].pop())

print(''.join(x[-1] for x in clean_stacks))