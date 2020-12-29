with open("day_11/day_11_input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

height = len(lines)
width = len(lines[0])

seats = {(y, x) for y in range(height) for x in range(width) if lines[y][x] == "L"}
directions = {(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}
visible_seats = {}
for seat in seats:
    visible = []
    for y_dir, x_dir in directions:
        y, x = seat[0] + y_dir, seat[1] + x_dir
        while True:
            if not (0 <= y < height and 0 <= x < width):
                break
            if lines[y][x] != ".":
                visible.append((y, x))
                break
            y += y_dir
            x += x_dir

    visible_seats[seat] = tuple(visible)

while True:
    new_state = [line.copy() for line in lines]
    for seat in seats:
        y, x = seat
        seat_status = lines[y][x]
        taken_seats = sum(lines[y0][x0] == "#" for y0, x0 in visible_seats[seat])
        if seat_status == "L" and taken_seats == 0:
            new_state[y][x] = "#"
        elif seat_status == "#" and taken_seats > 4:
            new_state[y][x] = "L"
    if new_state == lines:
        break
    else:
        lines = new_state

print(sum(line.count("#") for line in lines))
