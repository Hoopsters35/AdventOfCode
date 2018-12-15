def updategrid(grid, match):
    for row in range(match[3]):
        for col in range(match[4]):
            grid[match[1] + row][match[2] + col] += 1

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
        updategrid(grid, match)

    c = Counter(itertools.chain.from_iterable(grid))
    print(n*n - c[0] - c[1])

# 110,546
