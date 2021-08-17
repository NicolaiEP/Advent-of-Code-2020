from itertools import product, chain
import time

with open("day_17/day_17_input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

ITERATION_COUNT = 6
HEIGHT = len(lines)
WIDTH = len(lines[0])
DEPTH = 1
W_DEPTH = 1
n_dimensions = 4
relative_positions = set(product((-1, 0, 1), repeat=n_dimensions)) - {(0,) * n_dimensions}


def get_neighbours(pos):
    """Return a set of the n-dimensional neighbourhood positions of a given position pos."""
    neighbours = {tuple(sum(x) for x in zip(pos, offset)) for offset in relative_positions}
    return neighbours


# Saves the positions and their neighbour positions of the active cells in a dict
positions = [(x, y, z, w) for x in range(WIDTH) for y in range(HEIGHT)
             for z in range(DEPTH) for w in range(W_DEPTH)]


# APPROACH 1 (NEW):

# Adds cells with a count of nearby active cells. Active cells also gets an own dict with neighbour cells
interacted_cells = {}
active_cells = {}
for pos, state in zip(positions, chain(*lines)):
    if not state == "#":
        continue

    neighbours = get_neighbours(pos)
    active_cells[pos] = neighbours
    for neigbour in neighbours:
        if neigbour not in interacted_cells:
            interacted_cells[neigbour] = 1
        else:
            interacted_cells[neigbour] += 1

for _ in range(ITERATION_COUNT):
    start_time = time.time()

    # Adds dying cells to a set
    dying_cells = set()
    for cell in active_cells:
        if cell not in interacted_cells or not 2 <= interacted_cells[cell] <= 3:
            dying_cells.add(cell)

    # Adds new cells to a set
    new_cells = set()
    for cell, value in interacted_cells.items():
        if cell not in active_cells and value == 3:
            new_cells.add(cell)

    # Updates the pocket dimension with new cells
    for cell in new_cells:
        neighbours = get_neighbours(cell)
        active_cells[cell] = neighbours
        for neigbour in neighbours:
            if neigbour not in interacted_cells:
                interacted_cells[neigbour] = 1
            else:
                interacted_cells[neigbour] += 1

    # Updates the pocket dimension with dead cells
    for cell in dying_cells:
        neighbours = active_cells[cell]
        del active_cells[cell]
        for neigbour in neighbours:
            if interacted_cells[neigbour] == 1:
                del interacted_cells[neigbour]
            else:
                interacted_cells[neigbour] -= 1

    print(len(active_cells))
    print("Iteration time:", time.time() - start_time)

print("FINISH\n")


# APPROACH 2 (OLD):

# Saves the positions of active cells
active_cells = {pos for pos, state in zip(positions, chain(*lines)) if state == "#"}


for _ in range(6):
    start_time = time.time()
    # checked_cells = set()
    new_cells = set()
    dying_cells = set()
    # for cell in active_cells:
    #     if cell in checked_cells:
    #         continue
    #     neighbours = get_neighbourhood(cell)
    #     count = len(neighbours & active_cells)

    # Finds the cells to consider this cycle
    affected_cells = set(active_cells).union(*(get_neighbours(cell) for cell in active_cells))

    # Updates the sets for activation and deactivation
    for pos in affected_cells:
        # Counts active neighbours of pos
        count = len(get_neighbours(pos) & active_cells)

        # Decides if pos is going to activate, deactivate or be ignored
        active = pos in active_cells
        if active and not 2 <= count <= 3:
            dying_cells.add(pos)
        elif not active and count == 3:
            new_cells.add(pos)

    active_cells = new_cells | active_cells - dying_cells

    print(len(active_cells))
    print("Iteration time:", time.time() - start_time)

print("FINISH\n")


# APPROACH 3 (EVEN OLDER):
state_dict = {pos: state for pos, state in zip(positions, chain(*lines))}

for _ in range(6):
    start_time = time.time()
    new_state = state_dict.copy()

    # Finds the positions of the cells to consider this cycle
    affected_cells = set.union(*(get_neighbours(pos) for pos in state_dict.keys()))

    # Updates the states of the affected cells
    for pos in affected_cells:
        # Counts active neighbours
        count = sum(state_dict.get(p, ".") == "#" for p in get_neighbours(pos))
        cell_state = state_dict.get(pos, ".")

        # Updates the cell state according to the rules
        if cell_state == "#" and 2 <= count <= 3:
            continue
        elif cell_state == "." and count == 3:
            new_state[pos] = "#"
        else:
            new_state[pos] = "."

    state_dict = new_state

    print(sum(value == "#" for value in state_dict.values()))
    print("Iteration time:", time.time() - start_time)

print("FINISH\n")
