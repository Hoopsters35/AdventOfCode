with open ("day1inp.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    total = int(eval(f'{total}{line}'))

print(total)

# 411