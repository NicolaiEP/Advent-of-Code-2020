with open("day_5/day_5_input.txt") as f:
    boarding_passes = [b_pass for b_pass in f.read().splitlines()]

letters = {"F": "0", "B": "1", "L": "0", "R": "1"}

all_seat_IDs = set(row * 8 + col for row in range(128) for col in range(8))

seat_IDs = set()
for b_pass in boarding_passes:
    row = int("".join(letters[c] for c in b_pass[:7]), 2)
    col = int("".join(letters[c] for c in b_pass[7:]), 2)
    seat_IDs.add(row * 8 + col)

# Actually, I just printed out the missing numbers and found the odd one out with this:
# print(all_seat_IDs - seat_IDs)

missing = all_seat_IDs - seat_IDs
print([i for i in missing if not {i - 1, i + 1} & missing])
