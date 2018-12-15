def difby1(str1, str2):
    errs = 0
    for i, c in enumerate(str1):
        if str2[i] != c:
            errs += 1
        if errs > 1:
            return False
    return True if errs == 1 else False

def rembadchar(str1, str2):
    newstr = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            newstr += str1[i]
    return newstr

if __name__=='__main__':
    with open('day2inp.txt') as f:
        lines = f.readlines()

    found = False
    for line in lines:
        for test in lines:
            if difby1(line, test):
                print(rembadchar(line, test))
                found = True
                break
        if found:
            break
    print('None found')

# mphcuasvrnjzzkbgdtqeoylva
