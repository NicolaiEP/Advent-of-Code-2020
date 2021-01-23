with open("day_16/day_16_input.txt") as f:
    fields, my_ticket, other_tickets = f.read().split("\n\n")

valid_numbers = set()
for field in fields.split("\n"):
    *_, first_range, _, second_range = field.split()
    # NOTE: The walrus operator opens up for an alternative approach on the next two lines
    first_range = range(*[int(n) + i for i, n in enumerate(first_range.split("-"))])
    second_range = range(*[int(n) + i for i, n in enumerate(second_range.split("-"))])
    valid_numbers.update(first_range, second_range)

invalid_numbers = [int(n) for line in other_tickets.split("\n")[1:]
                   for n in line.split(",") if int(n) not in valid_numbers]

print(sum(invalid_numbers))
