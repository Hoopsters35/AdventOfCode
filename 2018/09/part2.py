DEBUG = False
def mod(num, mod):
    ans = num%mod
    if ans < 0:
        ans += mod
    return ans

def place_marble(marbles, marble, cur):
    spot = (cur+2)%len(marbles)
    marbles.insert(spot,marble)
    return spot

if __name__=='__main__':
    with open('day9inp.txt') as f:
        line = f.readline()

    import re
    regex = re.compile(r'(\d+)\D+(\d+)\D+')
    num_players, max_marble = tuple(map(lambda x : int(x), regex.match(line).groups()))
    max_marble *= 100

    from collections import deque
    players = [0 for i in range(num_players)]
    marbles = deque([0])
    
    curpos = 0
    if DEBUG:
        num_players = 10
        max_marble = 1618
    for marble in range(1, max_marble+1):
        curplayer = marble%num_players
        if marble % 23 == 0:
            players[curplayer] += marble
            marbles.rotate(7)
            players[curplayer] += marbles.popleft()
        else:
            marbles.rotate(-2)
            marbles.appendleft(marble)

    print(max(players))

# 3350093681
