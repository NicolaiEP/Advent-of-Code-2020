from itertools import product

with open("day_14/day_14_input.txt") as f:
    lines = [line.split(" = ") for line in f.read().splitlines()]

mask = ""
mem = {}
for assignment, value in lines:
    if assignment == "mask":
        mask = value
        continue
    address = int("".join(c for c in assignment if c.isdigit()))
    address = "{0:036b}".format(int(address))
    new_address = []
    value = int(value)
    for i, j in zip(mask, address):
        if i == "0":
            new_address.append(j)
        else:
            new_address.append(i)
    indexes = [i for i, bit in enumerate(new_address) if bit == "X"]
    for permutation in product("01", repeat=len(indexes)):
        for i, bit in zip(indexes, permutation):
            new_address[i] = bit
        address = int("".join(new_address), 2)
        mem[address] = value

print(sum(mem.values()))
