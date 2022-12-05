import pathlib
import string

cwd = pathlib.Path(__file__).parent.resolve()

with open(f'{cwd}/input.txt', 'r') as f:
    data = f.read().splitlines()

alphabet_lower_upper = string.ascii_lowercase + string.ascii_uppercase
alphabet_dict = {alphabet:idx+1 for idx,alphabet in enumerate(alphabet_lower_upper)}

score = 0
for i in range(0, len(data), 3):
    badge = (set(data[i]) & set(data[i+1]) & set(data[i+2])).pop()
    score += alphabet_dict.get(badge)
print(score)