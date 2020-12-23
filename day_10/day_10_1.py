with open("day_10/day_10_input.txt") as f:
    numbers = [0] + sorted([int(line) for line in f.read().splitlines()])

differences = [i - j for i, j in zip(numbers[1:], numbers[:-1])]
print(differences.count(1) * (differences.count(3) + 1))
