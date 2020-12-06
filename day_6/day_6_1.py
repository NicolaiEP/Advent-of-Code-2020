with open("day_6/day_6_input.txt") as f:
    groups = tuple(set(group.replace("\n", "")) for group in f.read().split("\n\n"))

print(sum(len(group) for group in groups))
