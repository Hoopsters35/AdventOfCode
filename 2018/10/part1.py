import matplotlib
import matplotlib.pyplot as plt
from time import sleep
from pylab import *
def display_nodes(positions):
    plt.plot([position[0] for position in positions], [position[1] for position in positions], 'ro')
    plt.show(block=True)

class Node:
    def __init__(self, data):
        self.position = [data[0], data[1]]
        self.velocity = (data[2], data[3])

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def __repr__(self):
        return f'Position: {self.position}, Velocity: {self.velocity}'

if __name__=='__main__':
    with open('day10inp.txt') as f:
        lines = f.readlines()

    import re
    regex = re.compile(r'\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+')
    matches = [tuple(map(lambda x : int(x), regex.match(line).groups())) for line in lines]
    nodes = [Node(match) for match in matches]

    matplotlib.interactive(True)

    ion()
    while True:
        display_nodes([node.position for node in nodes])
        for node in nodes:
            node.move()
        sleep(.01)

