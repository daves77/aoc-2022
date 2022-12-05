import pathlib
import string

cwd = pathlib.Path(__file__).parent.resolve()

with open(f'{cwd}/input.txt', 'r') as f:
    data = f.read().splitlines()

alphabet_lower_upper = string.ascii_lowercase + string.ascii_uppercase
alphabet_dict = {alphabet:idx+1 for idx,alphabet in enumerate(alphabet_lower_upper)}

score = 0
for el in data:
    first_compartment = el[:len(el)//2]
    second_compartment = el[len(el)//2:]
    item = (set(first_compartment) & set(second_compartment)).pop()
    score += alphabet_dict.get(item)

print(score)