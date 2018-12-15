class Cut:
    def __init__(self, num, fromL, fromT, wid, hei):
        self.id = num
        self.coords = (fromL, fromT)
        self.dims = (wid, hei)


if __name__=='__main__':
    with open('day3inp.txt') as f:
        lines = f.readlines()

    import re
    regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    line = lines[0]
    match = regex.match(line)
    matches = [regex.match(line).group() for line in lines]
    print(max([group[1] + group[3] for group in matches]))

