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

    totalsleep = {curid : sum(ids[curid]) for curid in ids.keys()}
    sleepyguard = sorted(list(totalsleep.items()), key=lambda x : x[1])[-1][0]
    maxsleep = max(ids[sleepyguard])
    badminutes = [i for i, j in enumerate(ids[sleepyguard]) if j == maxsleep]
    print(sleepyguard)
    print(badminutes[0])
    print(sleepyguard*badminutes[0])

# 39422
