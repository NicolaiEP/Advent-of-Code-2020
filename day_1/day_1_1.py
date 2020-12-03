from itertools import combinations

with open("day_1/day_1_input.txt") as f:
    numbers = tuple(int(line) for line in f.read().splitlines())

print(sum(i * j for i, j in combinations(numbers, 2) if i + j == 2020))
