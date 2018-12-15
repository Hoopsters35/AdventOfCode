def processline(text):
    lettercounts = {}
    for letter in text:
        if letter in lettercounts.keys():
            lettercounts[letter] += 1
        else:
            lettercounts[letter] = 1
    return lettercounts

def hastwo(counts):
    for key in counts.keys():
        if counts[key] is 2:
            return True
    return False

def hasthree(counts):
    for key in counts.keys():
        if counts[key] is 3:
            return True
    return False

if __name__=='__main__':
    with open('day2inp.txt') as f:
        lines = f.readlines()

    numtwos = 0
    numthrees = 0

    for line in lines:
        counts = processline(line)
        if hastwo(counts):
            numtwos += 1
        if hasthree(counts):
            numthrees += 1

    print(numtwos*numthrees)

# 7533
