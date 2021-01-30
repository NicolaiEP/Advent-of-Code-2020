import re

with open("day_18/day_18_input.txt") as f:
    lines = [re.sub(r"(\d+)", r"(\1)", line).replace(" + ", ".__add__").replace(" * ", ".__mul__")
             for line in f.read().splitlines()]

print(sum(eval(line) for line in lines))
