def updategrid(grid, match, put):
    overlap = set()
    for row in range(match[3]):
        for col in range(match[4]):
            y = match[1] + row
            x = match[2] + col
            if grid[y][x] != 0:
                overlap.add(grid[y][x])
            grid[y][x] = put
    return overlap

if __name__=='__main__':
    with open('day3inp.txt') as f:
        lines = f.readlines()

    import re
    from collections import Counter
    import itertools
    regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    matches = [tuple(map(lambda x : int(x), regex.match(line).groups())) for line in lines]

    n = 1000
    grid = [[0 for i in range(n)] for j in range(n)]
    for match in matches:
        overlap = updategrid(grid, match, match[0])
        if overlap:
            overlap.add(match[0])
            if -1 in overlap:
                overlap.remove(-1) 
            for num in overlap:
                updategrid(grid, matches[num-1], -1)

    c = Counter(itertools.chain.from_iterable(grid))
    print(c)

# 819
