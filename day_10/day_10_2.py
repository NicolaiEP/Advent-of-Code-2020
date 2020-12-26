from functools import lru_cache
with open("day_10/day_10_input.txt") as f:
    numbers = {int(line) for line in f.read().splitlines()}
end = max(numbers)


@lru_cache
def count_possible(n):
    total = 0
    for i in {n + 1, n + 2, n + 3} & numbers:
        if i == end:
            total += 1
        else:
            total += count_possible(i)
    return total


print(count_possible(0))
