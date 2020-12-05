with open("day_5/day_5_input.txt") as f:
    boarding_passes = [b_pass for b_pass in f.read().splitlines()]

letters = {"F": "0", "B": "1", "L": "0", "R": "1"}

seat_IDs = []
for b_pass in boarding_passes:
    row = int("".join(letters[c] for c in b_pass[:7]), 2)
    col = int("".join(letters[c] for c in b_pass[7:]), 2)
    seat_IDs.append(row * 8 + col)

print(max(seat_IDs))
