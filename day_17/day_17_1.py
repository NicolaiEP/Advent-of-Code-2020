from itertools import product, chain

with open("day_17/day_17_input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

HEIGHT = len(lines)
WIDTH = len(lines[0])
DEPTH = 1


def get_neighbourhood(pos):
    """Return a set of the n-dimensional neighbourhood positions of a given position pos."""
    n_dimensions = len(pos)
    relative_positions = set(product((-1, 0, 1), repeat=n_dimensions)) - {(0,) * n_dimensions}
    neighbours = {tuple(sum(x) for x in zip(pos, offset)) for offset in relative_positions}
    return neighbours


# Saves the positions and the initial states of the cubes in a dict
positions = [(x, y, z) for x in range(WIDTH) for y in range(HEIGHT) for z in range(DEPTH)]
state_dict = {pos: state for pos, state in zip(positions, chain(*lines))}

for _ in range(6):
    new_state = state_dict.copy()

    # Finds the positions of the cubes to consider this cycle
    affected_cubes = set.union(*(get_neighbourhood(pos) for pos in state_dict.keys()))

    # Updates the states of the affected cubes
    for pos in affected_cubes:
        # Counts active neighbours
        count = sum(state_dict.get(p, ".") == "#" for p in get_neighbourhood(pos))
        cube_state = state_dict.get(pos, ".")

        # Updates the cube state according to the rules
        if cube_state == "#" and 2 <= count <= 3:
            continue
        elif cube_state == "." and count == 3:
            new_state[pos] = "#"
        else:
            new_state[pos] = "."

    state_dict = new_state

print(sum(value == "#" for value in state_dict.values()))
