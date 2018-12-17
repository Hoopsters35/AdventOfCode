xmax = 349
ymax = 359

def insertcoord(grid, coord):
    for x in range(xmax):
        for y in range(ymax):
            md = mandist((x,y), coord)
            grid[x][y] += md

def mandist(cord1, cord2):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])


if __name__=='__main__':
    with open('day6inp.txt') as f:
        lines = f.readlines()
    
    coords = [tuple(map(lambda x : int(x), line.strip().split(', '))) for line in lines]
    # Grid is 349 x 359
    # 50 coordinates given
    grid = [[0 for i in range(ymax)] for j in range(xmax)]
    for coord in coords:
        insertcoord(grid, coord)

    import itertools
    target = 10000
    print(len([i for i in itertools.chain.from_iterable(grid) if i < target]))

# 36238 too high
