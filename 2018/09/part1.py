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

    players = [0 for i in range(num_players)]
    marbles = [0]
    curpos = 0
    for marble in range(1, max_marble+1):
        curplayer = marble%num_players
        if marble % 23 == 0:
            players[curplayer] += marble
            pos_to_remove = mod(curpos-7, len(marbles))
            removed_marb = marbles[pos_to_remove]
            players[curplayer] += removed_marb
            marbles.pop(pos_to_remove)
            curpos = pos_to_remove
        else:
            curpos = place_marble(marbles, marble, curpos)

    print(max(players))

# 404611
