from math import sin, cos, radians
with open("day_12/day_12_input.txt") as f:
    instructions = tuple((line[0], int(line[1:])) for line in f.read().splitlines())

directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
position = [0, 0]
waypoint = [10, 1]

for action, value in instructions:
    if action in directions:
        waypoint[0] += value * directions[action][0]
        waypoint[1] += value * directions[action][1]
    elif action == "F":
        position[0] += value * waypoint[0]
        position[1] += value * waypoint[1]
    else:
        x, y = waypoint

        sign = [1, -1][action == "R"]
        sine = round(sin(sign * radians(value)))
        cosine = round(cos(sign * radians(value)))

        waypoint[0] = x * cosine - y * sine
        waypoint[1] = x * sine + y * cosine


print(abs(position[0]) + abs(position[1]))
