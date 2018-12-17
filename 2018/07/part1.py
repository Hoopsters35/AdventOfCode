if __name__=='__main__':
    with open('day7inp.txt') as f:
        lines = f.readlines()

    import re
    from string import ascii_uppercase
    regex = re.compile(r'Step (\w) must be finished before step (\w).*\.')
    edges = [(regex.match(line).groups()) for line in lines]
    reqs = {char : set() for char in ascii_uppercase}
    for edge in edges:
        reqs[edge[1]].add(edge[0])

    order = []
    while len(reqs) > 0:
        pos = sorted(item[0] for item in reqs.items() if len(item[1]) == 0)
        reqs.pop(pos[0])
        order.append(pos[0])
        for char in ascii_uppercase:
            if char in reqs.keys() and pos[0] in reqs[char]:
                reqs[char].remove(pos[0])

    print(''.join(order))
    
#ABDCJLFMNVQWHIRKTEUXOZSYPG

