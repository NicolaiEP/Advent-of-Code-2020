with open("day_9/day_9_input.txt") as f:
    numbers = [int(n) for n in f.read().splitlines()]

preamble = numbers[:25]
rest = numbers[25:]

invalid_number = 0

for n in rest:
    if not any([n - m in set(preamble) - {m} for m in preamble]):
        print(n)
        invalid_number = n
        break
    del preamble[0]
    preamble.append(n)

# This is a kind of brute forcing and I don't like it, but it worked
found_set = False
for i in range(len(numbers)):
    for j in range(2, len(numbers[i:])):
        contiguous_set = numbers[i:i + j]
        if sum(contiguous_set) == invalid_number:
            found_set = True
            print(min(contiguous_set) + max(contiguous_set))
            break
    if found_set:
        break
