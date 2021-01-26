with open("day_16/day_16_input.txt") as f:
    field_numbers, my_ticket, other_tickets = f.read().split("\n\n")

# Creates number lists from the strings
my_ticket = [int(n) for n in my_ticket.split("\n")[1].split(",")]
other_tickets = [[int(n) for n in line.split(",")] for line in other_tickets.split("\n")[1:]]

# Creates a set and dictionary for valid numbers
field_ranges = {}
for field in field_numbers.split("\n"):
    *field_name, first_range, _, second_range = field.split()
    first_range = range(*[int(n) + i for i, n in enumerate(first_range.split("-"))])
    second_range = range(*[int(n) + i for i, n in enumerate(second_range.split("-"))])
    field_ranges[" ".join(field_name).rstrip(":")] = set(first_range) | set(second_range)

# Transposes the valid ticket list
valid_numbers = set.union(*field_ranges.values())
valid_tickets = [ticket for ticket in other_tickets if set(ticket) <= valid_numbers]
field_numbers = [set(field) for field in zip(*valid_tickets)]

# Finds the indexes of each field
field_positions = {}
while len(field_positions) < len(my_ticket):
    for i, field in enumerate(field_numbers):
        potential_fields = []
        for field_name, values in field_ranges.items():
            if field.issubset(values):
                potential_fields.append(field_name)
        if len(potential_fields) == 1:
            field_name = potential_fields[0]
            field_positions[field_name] = i
            del field_ranges[field_name]

# Finds the product
product = 1
for field_name, i in field_positions.items():
    if field_name.startswith("departure"):
        product *= my_ticket[i]

print(product)
