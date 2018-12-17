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

    # Find all ids that are on edges and have infinite area
    rem = set()
    for x in range(xmax):
        rem.add(grid[x][0][0])
        rem.add(grid[x][ymax-1][0])
    for y in range(1, ymax-1):
        rem.add(grid[0][y][0])
        rem.add(grid[xmax-1][y][0])

    gridofids = [cell[0] for x in grid for cell in x if cell[0] not in rem]

    import itertools
    from collections import Counter
    totals = Counter(gridofids)
    print(sorted(totals.items(), key = lambda x : x[1]))

# 3909
