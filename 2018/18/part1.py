GRID_SIZE = 50
OPEN = '.'
TREES = '|'
LUMBER_YARD = '#'

def add_to_counts(counts, cur):
    if cur == OPEN:
        counts[0] += 1
    if cur == TREES:
        counts[1] += 1
    if cur == LUMBER_YARD:
        counts[2] += 1

def in_bounds(coords):
    return coords[0] < GRID_SIZE and coords[1] < GRID_SIZE

def get_rel_square(grid, start, direction):
    new_coords = (start[0] + direction[0], start[1] + direction[1])
    return grid[new_coords[0]][new_coords[1]] if in_bounds(new_coords) else None

def count_surroundings(grid, cur_square, directions):
    counts = list(0 for _ in range(3))
    for cur_dir in directions:
        new_sq = get_rel_square(grid, cur_square, cur_dir)
        if new_sq:
            add_to_counts(counts, new_sq)
    return counts 

def next_gen(square, counts):
    new = square
    if square == OPEN:
        if counts[1] >= 3:
            new = TREES
    elif square == TREES:
        if counts[2] >= 3:
            new = LUMBER_YARD
    elif square == LUMBER_YARD:
        if counts[1] == 0 or counts[2] == 0:
            new = OPEN
    return new

def get_next_gen(grid, dirs):
    #TODO

if __name__=='__main__':
    with open('day18inp.txt') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    dirs = ((-1, 1),  (0, 1),  (1, 1),
            (-1, 0),           (1, 0),
            (-1, -1), (0, -1), (1, -1))
    print(lines[0][0:3])
    print(lines[1][0:3])
    print(lines[2][0:3])
    counts = count_surroundings(lines, (1, 1), dirs)
    print(counts)
    print(next_gen(lines[1][1], counts))

    num_mins = 10
    #for _ in range(num_mins):
        #lines = get_next_gen(lines, dirs)

    import itertools
    from collections import Counter
    totals = Counter(itertools.chain.from_iterable(lines))
    print(totals[TREES] * totals[LUMBER_YARD])
