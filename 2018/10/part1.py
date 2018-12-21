import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
import numpy as np

def update_plot(i, nodes, scat):
    positions = [node.position for node in nodes]
    scat.set_offsets(([position[0] for position in positions], [position[1] for position in positions]))

    return scat,

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

    numframes = 100

    fig = plt.figure()
    x, y = [node.position for node in nodes]
    print(x)
    positions = [node.position for node in nodes]
    scat = plt.scatter([position[0] for position in positions], [position[1] for position in positions], s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=range(numframes), fargs=(nodes, scat))

    plt.show()
    #while True:
        #plt.pause(.0001)
        #for node in nodes:
            #node.move()
        #positions = [node.position for node in nodes]
        ##sc.scatter([position[0] for position in positions], [position[1] for position in positions])

