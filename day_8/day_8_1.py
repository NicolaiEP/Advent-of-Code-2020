with open("day_8/day_8_input.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

visited = set()
accumulator = 0
index = 0
while True:
    if index in visited:
        print(accumulator)
        break
    else:
        visited.add(index)
        operator, argument = lines[index]
        if operator == "acc":
            accumulator += int(argument)
            index += 1
        elif operator == "jmp":
            index += int(argument)
        else:
            index += 1
