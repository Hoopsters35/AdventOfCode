def explode(c1, c2):
    return (c1.lower() == c2 or c1.upper() == c2) and c1 != c2

with open('day5inp.txt') as f:
    line = list(f.readline())
    line.pop()

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
print(len(line))

# 9704
