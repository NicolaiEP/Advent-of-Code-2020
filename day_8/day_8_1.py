with open("day_8/day_8_input.txt") as f:
    lines = list(enumerate(line.split() for line in f.read().splitlines()))

visited = set()
accumulator = 0
index = 0
while True:
    i, instruction = lines[index]
    if i in visited:
        print(accumulator)
        break
    elif instruction[0] == "acc":
        accumulator += int(instruction[1])
        index += 1
    elif instruction[0] == "jmp":
        index += int(instruction[1])
    else:
        index += 1
    visited.add(i)
