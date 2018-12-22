class Sample:
    def __init__(self, before, codes, after):
        self.before = before
        self.codes = codes
        self.after = after

    def __repr__(self):
        return f'Before: {self.before}\nCodes: {self.codes}\nAfter: {self.after}'


class Functions:
    @staticmethod
    def addr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] + nums[codes[2]])
        return new_nums

    @staticmethod
    def addi(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] + nums[2])
        return new_nums

    @staticmethod
    def mulr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] * nums[codes[2]])
        return new_nums

    @staticmethod
    def muli(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] * nums[2])
        return new_nums

    @staticmethod
    def banr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] & nums[codes[2]])
        return new_nums

    @staticmethod
    def bani(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] & nums[2])
        return new_nums

    @staticmethod
    def borr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] | nums[codes[2]])
        return new_nums

    @staticmethod
    def bori(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[codes[1]] | nums[2])
        return new_nums

    @staticmethod
    def setr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(codes[nums[1]])
        return new_nums

    @staticmethod
    def seti(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(nums[1])
        return new_nums

    @staticmethod
    def gtir(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[1] > nums[codes[2]] else 0)
        return new_nums

    @staticmethod
    def gtri(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[codes[1]] > nums[2] else 0)
        return new_nums

    @staticmethod
    def gtrr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[codes[1]] > nums[codes[2]] else 0)
        return new_nums

    @staticmethod
    def eqir(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[1] == nums[codes[2]] else 0)
        return new_nums

    @staticmethod
    def eqri(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[codes[1]] == nums[2] else 0)
        return new_nums

    @staticmethod
    def eqrr(codes, nums):
        new_nums = []
        new_nums.append(nums[0])
        new_nums.append(nums[1])
        new_nums.append(nums[2])
        new_nums.append(1 if nums[codes[1]] == nums[codes[2]] else 0)
        return new_nums


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

def exec_function(fun, codes, nums):
    eval('print(nums)')
    return eval(f'Functions.{fun}(codes, nums)')

if __name__=='__main__':
    with open('day16inp.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    #samples = process_input(lines)
    #print(samples[0])
    function_list = [func for func in dir(Functions) if callable(getattr(Functions, func)) and not '_' in func]
    print(exec_function('addi', [9,2,1,2], [3, 2, 1, 1]))
