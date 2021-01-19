with open("day_14/day_14_input.txt") as f:
    lines = [line.split(" = ") for line in f.read().splitlines()]

mask = ""
mem = {}
for assignment, value in lines:
    if assignment == "mask":
        mask = value
        continue
    address = int("".join(c for c in assignment if c.isdigit()))
    value = "{0:036b}".format(int(value))
    new_value = []
    for i, j in zip(mask, value):
        if i != "X":
            new_value.append(i)
        else:
            new_value.append(j)
    mem[address] = int("".join(new_value), 2)

print(sum(mem.values()))
