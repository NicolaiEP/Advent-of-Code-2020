with open("day_7/day_7_input.txt") as f:
    lines = {(color, bags) for color, bags in
             (line.split(" bags contain ") for line in f.read().splitlines())}

open_set = {"shiny gold"}
closed_set = set()

while open_set:
    comp_color = next(iter(open_set))
    new_lines = set()
    for color, bags in lines:
        if comp_color in bags:
            open_set.add(color)
        else:
            new_lines.add((color, bags))

    lines = new_lines
    open_set.remove(comp_color)
    closed_set.add(comp_color)

closed_set.remove("shiny gold")  # Removes this color since we won't count it
print(len(closed_set))
