from itertools import combinations

with open("day_1/day_1_input.txt") as f:
    numbers = tuple(int(line) for line in f.read().splitlines())

print(sum(i * j * k for i, j, k in combinations(numbers, 3) if i + j + k == 2020))
