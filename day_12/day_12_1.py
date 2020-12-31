from collections import deque
with open("day_12/day_12_input.txt") as f:
    instructions = tuple((line[0], int(line[1:])) for line in f.read().splitlines())

directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
direction_queue = deque("ESWN")
position = [0, 0]

for action, value in instructions:
    if action in directions:
        position[0] += value * directions[action][0]
        position[1] += value * directions[action][1]
    elif action == "F":
        current_direction = direction_queue[0]
        position[0] += value * directions[current_direction][0]
        position[1] += value * directions[current_direction][1]
    else:
        sign = [1, -1][action == "R"]
        direction_queue.rotate(sign * value // 90)

print(abs(position[0]) + abs(position[1]))
