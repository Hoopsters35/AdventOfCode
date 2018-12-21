PLANT = '#'
NO_PLANT = '.'

def get_char(index, negstate, posstate):
    char = ''
    if index < 0:
        if abs(index) <= len(negstate):
            char = negstate[abs(index)-1]
        else:
            char = NO_PLANT
    else:
        if index < len(posstate):
            char = posstate[index]
        else:
            char = NO_PLANT
    return char

def put_char(c, i, negstate, posstate):
    if i < 0:
        negstate.insert(abs(i)-1, c)
    else:
        posstate.insert(i, c)

def matches_rule(segment, rules):
    if ''.join(segment) in rules.keys():
        return ''.join(segment)
    return None

def get_seg(target, negstate, posstate):
    segment = []
    for offset in range(-2, 3):
        index = target + offset
        char = get_char(index, negstate, posstate)
        segment.append(char)
    return segment

def strip_edges(negstate, posstate):
    i = -1
    while len(negstate) > 0 and negstate[i] == NO_PLANT:
        negstate.pop()
    while len(posstate) > 0 and posstate[i] == NO_PLANT:
        posstate.pop()

def apply_rules(negstate, posstate, rules):
    new_neg = []
    new_pos = []
    # iterate through negatives in abs value order
    for i in range(-len(negstate)-2, len(posstate)+2):
        segment = get_seg(i, negstate, posstate)
        char = ''
        if matches_rule(segment, rules):
            char = rules[''.join(segment)]
        else:
            char = get_char(i, negstate, posstate)
        put_char(char, i, new_neg, new_pos)
    strip_edges(new_neg, new_pos)
    return new_neg, new_pos

def get_flower_numbers(negstate, posstate):
    total = []
    for i in range(-len(negstate), len(posstate)):
        if get_char(i, negstate, posstate) == PLANT:
            total.append(i)
    return total

if __name__=='__main__':
    with open('day12inp.txt') as f:
        lines = f.readlines()

    posstate = list(lines[0][15:].strip())
    negstate = []

    lines = [line.strip().split(' => ') for line in lines[2:]]
    rules = {line[0] : line[1] for line in lines}

    num_generations = 50000000000
    for _ in range(num_generations):
        negstate, posstate = apply_rules(negstate, posstate, rules)

    print(sum(get_flower_numbers(negstate, posstate)))

#
