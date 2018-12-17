xmax = 349
ymax = 359

def insertcoord(grid, coord, dig):
    print(f'Working on coordinate {dig}')
    for x in range(xmax):
        for y in range(ymax):
            md = mandist((x,y), coord)
            if md < grid[x][y][1]:
                grid[x][y] = [dig, md]
            elif md == grid[x][y][1]:
                grid[x][y] = [-1, md]

def mandist(cord1, cord2):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])


if __name__=='__main__':
    with open('day6inp.txt') as f:
        lines = f.readlines()
    
    coords = [tuple(map(lambda x : int(x), line.strip().split(', '))) for line in lines]
    # Grid is 349 x 359
    # 50 coordinates given
    grid = [[[-1, 1000] for i in range(ymax)] for j in range(xmax)]
    for i, coord in enumerate(coords):
        insertcoord(grid, coord, i)

    gridofids = [cell[0] for x in grid for cell in x]

    import itertools
    from collections import Counter
    totals = Counter(i for i in list(itertools.chain.from_iterable(gridofids)))
    print(max(totals))
