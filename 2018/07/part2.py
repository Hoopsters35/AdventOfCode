from string import ascii_uppercase
def timeforchar(char):
    return 61 + ascii_uppercase.index(char)

def removeall(reqs, c):
    for char in ascii_uppercase:
        if char in reqs.keys() and c in reqs[char]:
            reqs[char].remove(c)

if __name__=='__main__':
    with open('day7inp.txt') as f:
        lines = f.readlines()

    import re
    regex = re.compile(r'Step (\w) must be finished before step (\w).*\.')
    edges = [(regex.match(line).groups()) for line in lines]
    reqs = {char : set() for char in ascii_uppercase}
    for edge in edges:
        reqs[edge[1]].add(edge[0])

    numworkers = 5
    order = []
    counter = -1 # start at -1 to ease edge case
    workers = [None for i in range(numworkers)]
    inprocess = set()
    while len(reqs) > 0:
        # Reduce time on each work
        counter += 1
        workers = list(map(lambda x : [x[0], x[1]-1] if x else None, workers))
        finished = [(i, w[0]) for i, w in enumerate(workers) if w and w[1] == 0]
        for idx, finish in finished:
            workers[idx] = None
            reqs.pop(finish)
            order.append(finish)
            removeall(reqs, finish)

        pos = sorted(item[0] for item in reqs.items() if item[0] not in inprocess and len(item[1]) == 0)
        # Populate work for workers
        while pos and None in workers:
            workers[workers.index(None)] = [pos[0], timeforchar(pos[0])]
            inprocess.add(pos[0])
            pos.remove(pos[0])

    print(counter)
    
# 896 incorrect

