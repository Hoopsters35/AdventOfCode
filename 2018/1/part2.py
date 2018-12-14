with open ("day1inp.txt") as f:
    lines = f.readlines()

total = 0
seen = set()
dupfound = False
while not dupfound:
    for line in lines:
        seen.add(total)
        total = int(eval(f'{total}{line}'))
        if total in seen:
            dupfound = True
            print(f'Duplicate found: {total}')
            break

# 56360