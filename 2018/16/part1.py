class Sample:
    def __init__(self, before, codes, after):
        self.before = before
        self.codes = codes
        self.after = after

    def __repr__(self):
        return f'Before: {self.before}\nCodes: {self.codes}\nAfter: {self.after}'


class Functions:
    def addr(nums):

def process_input(lines):
    samples = []
    i = 0
    while 'Before' in lines[i]:
        before = list(map(lambda x : int(x), lines[i][9:19].split(', ')))
        i += 1
        codes = list(map(lambda x : int(x), lines[i].split()))
        i += 1
        after = list(map(lambda x : int(x), lines[i][9:19].split(', ')))
        i += 1
        samples.append(Sample(before, codes, after))
    return samples

if __name__=='__main__':
    with open('day16inp.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    samples = process_input(lines)
    print(samples[0])
