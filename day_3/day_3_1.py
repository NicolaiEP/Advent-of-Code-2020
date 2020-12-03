with open("day_3/day_3_input.txt") as f:
    terrain = tuple(line for line in f.read().splitlines())

print(sum(row[3 * i % len(row)] == "#" for i, row in enumerate(terrain)))
