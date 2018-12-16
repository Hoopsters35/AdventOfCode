def explode(c1, c2):
    return (c1.lower() == c2 or c1.upper() == c2) and c1 != c2

with open('day5inp.txt') as f:
    line = f.readline()
    line = line[0:len(line)-1]

print(len(line))

