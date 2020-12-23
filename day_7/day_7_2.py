with open("day_7/day_7_input.txt") as f:
    bag_dict = {color: bags[:-1].split(", ") for color, bags in
                (line.split(" bags contain ") for line in f.read().splitlines())}


def number_of_bags(bag_color):
    bags = bag_dict[bag_color]
    if bags[0] == "no other bags":
        return 0
    bags = [(int(n), " ".join(color[:-1])) for n, *color in (bag.split() for bag in bags)]
    return sum(bag[0] * (1 + number_of_bags(bag[1])) for bag in bags)


print(number_of_bags("shiny gold"))
