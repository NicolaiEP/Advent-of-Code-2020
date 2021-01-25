with open("day_16/day_16_input.txt") as f:
    fields, my_ticket, other_tickets = f.read().split("\n\n")

valid_numbers = set()
field_ranges = {}
for field in fields.split("\n"):
    *field_name, first_range, _, second_range = field.split()
    first_range = range(*[int(n) + i for i, n in enumerate(first_range.split("-"))])
    second_range = range(*[int(n) + i for i, n in enumerate(second_range.split("-"))])
    valid_numbers.update(first_range, second_range)
    field_ranges[" ".join(field_name).rstrip(":")] = set(first_range) | set(second_range)


valid_tickets = []
for ticket in other_tickets.split("\n")[1:]:
    ticket = [int(n) for n in ticket.split(",")]
    if all(n in valid_numbers for n in ticket):
        valid_tickets.append(ticket)

fields = [set(field) for field in zip(*valid_tickets)]

field_positions = {}
number_of_fields = len(field_ranges)
while len(field_positions) < number_of_fields:
    for i, field in enumerate(fields):
        potential_fields = []
        for field_name, values in field_ranges.items():
            if field.issubset(values):
                potential_fields.append(field_name)
        if len(potential_fields) == 1:
            field_name = potential_fields[0]
            field_positions[field_name] = i
            del field_ranges[field_name]

my_ticket = [int(n) for n in my_ticket.split("\n")[1].split(",")]
product = 1
for field_name, i in field_positions.items():
    if field_name.startswith("departure"):
        product *= my_ticket[i]

print(product)
