if __name__=='__main__':
    with open('day12inp.txt') as f:
        lines = f.readlines()

    buf = 20
    empty_plants = ''.join(['.' for _ in range(buf)])
    state = f'{empty_plants}{lines[0][15:].strip()}{empty_plants}'
    lines = [line.strip().split(' => ') for line in lines[2:]]
    rules = {line[0] : line[1] for line in lines}
    print(state)
    print(state[buf])
