import re
def getid(note):
    return int(re.match(r'\D*(\d+)\D*', note[1]).groups()[0])

def processshift(elems, ids, i):
    curid = getid(elems[i])
    i += 1
    awake = True
    minute = 0
    while i < len(elems) and elems[i][1][0] != 'G':
        # Populate ids for this shift
        changemin = elems[i][0].minute
        while minute < changemin:
            if not awake:
                ids[curid][minute] += 1
            minute += 1
        awake = not awake
        i += 1
    while not awake and minute < 60:
        ids[curid][minute] += 1
        minute += 1

    return i

if __name__=='__main__':
    with open('day4inp.txt') as f:
        lines = f.readlines()

    import datetime
    regex = re.compile(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)')
    matches = [regex.match(line).groups() for line in lines]
    matches = [tuple(x if i == 5 else int(x) for i,x in enumerate(match)) for match in matches]
    elems = [(datetime.datetime(year=elem[0], month=elem[1], day=elem[2], hour=elem[3], minute=elem[4]), elem[5]) for elem in matches]
    elems.sort(key=lambda x : x[0])
    ids = {getid(elem) : [0 for i in range(60)] for elem in elems if elem[1][0] == 'G'}

    i = 0
    while i < len(elems):
        i = processshift(elems, ids, i)

    mostsleepmins = {curid : max(ids[curid]) for curid in ids}
    guard_with_worst_minute = sorted(list(mostsleepmins.items()), key = lambda x : x[1])[-1][0]
    guards_worst_minute = [i for i, j in enumerate(ids[guard_with_worst_minute]) if j == mostsleepmins[guard_with_worst_minute]]
    print(guard_with_worst_minute)
    print(guards_worst_minute)
    print(guard_with_worst_minute*guards_worst_minute[0])

# 65474
