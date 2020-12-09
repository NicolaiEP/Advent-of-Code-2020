with open("day_8/day_8_input.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

visited = set()
accumulator = 0
index = 0
potential_errors = []
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
            potential_errors.append((index, (operator, argument)))
            index += int(argument)
        else:
            potential_errors.append((index, (operator, argument)))
            index += 1


for i, instruction in potential_errors:
    if instruction[0] == "jmp":
        lines[i][0] = "nop"
    else:
        lines[i][0] = "jmp"

    visited = set()
    accumulator = 0
    index = 0
    potential_errors = []
    while True:
        if index in visited:
            break
        elif index == len(lines):
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
    lines[i][0] = instruction[0]
