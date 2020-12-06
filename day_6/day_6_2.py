with open("day_6/day_6_input.txt") as f:
    groups = [map(set, group.split("\n")) for group in f.read().split("\n\n")]

print(sum(len(set.intersection(*group)) for group in groups))
