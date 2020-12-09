with open("day_9/day_9_input.txt") as f:
    numbers = [int(n) for n in f.read().splitlines()]

preamble = numbers[:25]
rest = numbers[25:]

for n in rest:
    if not any([n - m in set(preamble) - {m} for m in preamble]):
        print(n)
        break
    del preamble[0]
    preamble.append(n)
