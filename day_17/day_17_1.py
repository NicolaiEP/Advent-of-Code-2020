from itertools import product, chain
import time

with open("day_17/day_17_input.txt") as f:
    lines = [list(line) for line in f.read().splitlines()]

ITERATION_COUNT = 6
HEIGHT = len(lines)
WIDTH = len(lines[0])
DEPTH = 1
n_dimensions = 3
relative_positions = set(product((-1, 0, 1), repeat=n_dimensions)) - {(0,) * n_dimensions}


def get_neighbours(pos):
    """Return a set of the n-dimensional neighbourhood positions of a given position pos."""
    neighbours = {tuple(sum(x) for x in zip(pos, offset)) for offset in relative_positions}
    return neighbours


# Saves the positions and their neighbour positions of the active cells in a dict
positions = [(x, y, z) for x in range(WIDTH) for y in range(HEIGHT)
             for z in range(DEPTH)]


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
