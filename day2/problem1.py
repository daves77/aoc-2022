################ PROBLEM 1 ##################
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}

table = [
    [4, 8 ,3],
    [1, 5, 9],
    [7, 2, 6]
]

points = sum(table[mapping.get(el[0])][mapping.get(el[2])] for el in data)
print(points)


################ PROBLEM 2 ##################

with open('input.txt', 'r') as f:
    data = f.read().splitlines()



mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}

table = [
    [3, 1 ,2],
    [4, 5, 6],
    [8, 9, 7]
]

points = sum(table[mapping.get(el[2])][mapping.get(el[0])] for el in data)
print(points)
