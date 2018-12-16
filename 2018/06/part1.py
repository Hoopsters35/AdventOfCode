if __name__=='__main__':
    with open('day6inp.txt') as f:
        lines = f.readlines()
    
    coords = [tuple(map(lambda x : int(x), line.strip().split(', '))) for line in lines]
    print(coords)
