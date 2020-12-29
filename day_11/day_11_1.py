with open("day_11/day_11_input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

height = len(lines)
width = len(lines[0])

seats = {(y, x) for y in range(height) for x in range(width) if lines[y][x] == "L"}
relative_positions = {(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}

while True:
    new_state = [line.copy() for line in lines]
    for seat in seats:
        y, x = seat
        seat_status = lines[y][x]
        neighbour_seats = {(y + pos[0], x + pos[1]) for pos in relative_positions} & seats
        taken_seats = sum(lines[y0][x0] == "#" for y0, x0 in neighbour_seats)
        if seat_status == "L" and taken_seats == 0:
            new_state[y][x] = "#"
        elif seat_status == "#" and taken_seats > 3:
            new_state[y][x] = "L"
    if new_state == lines:
        break
    else:
        lines = new_state

print(sum(line.count("#") for line in lines))
