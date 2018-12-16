def explode(c1, c2):
    return (c1.lower() == c2 or c1.upper() == c2) and c1 != c2

def cleanline(line):
    i = 0
    j = i + 1
    while j < len(line):
        if explode(line[i], line[j]):
            line.pop(j)
            line.pop(i)
            if i != 0:
                j -= 1
                i -= 1
        else:
            i += 1
            j += 1

if __name__=='__main__':
    from string import ascii_lowercase
    with open('day5inp.txt') as f:
        line = list(f.readline())
        line.pop()
    
    a = {a : 0 for a in ascii_lowercase}
    for c in ascii_lowercase:
        l = [char for char in list(line) if char.lower() != c]
        print(f'Working on {c}...')
        cleanline(l)
        a[c] = len(l)

    print(sorted(list(a.items()), key = lambda x : x[1])[0])

# 6942
