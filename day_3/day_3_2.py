with open("day_3.txt") as f:
    terrain = tuple(line for line in f.read().splitlines())

product = 1
for n in (1, 3, 5, 7):
    product *= sum(row[n * i % len(row)] == "#" for i, row in enumerate(terrain))
product *= sum(row[i % len(row)] == "#" for i, row in enumerate(terrain[::2]))
print(product)
