from settings import *
from algorithms.node import Node
from random import randint


class _Node(Node):
    def __init__(self, pos=None, parent=None):
        Node.__init__(self, pos, parent)
        self.visited = False

class BFS:
    def __init__(self, grid, random = False):
        self.cueList = []
        self.nodeList = []
        self.grid = grid
        for i in range(0, HEIGTH, SQUARE):
            for j in range(0, WIDTH, SQUARE):
                node = _Node((i, j))
                if (i, j) == grid.start:
                    self.start = node
                    self.cueList.append(node)
                self.nodeList.append(node)
        self.end = _Node(self.grid.end)
        self.path = []
        self.random = random

    def run(self):
        if len(self.cueList) == 0:
            return True
        if self.random:
            pos = randint(0, len(self.cueList)-1)
        else:
            pos = 0
        current_node = self.cueList.pop(pos)
        current_node.visited = True
        if current_node == self.end:
            self.path = []
            current = current_node
            while current is not None:
                self.path.append(current.pos)
                current = current.parent
            return True
        
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            pos_x = current_node.pos[0] + SQUARE * new_position[0]
            pos_y = current_node.pos[1] + SQUARE * new_position[1]
            new_pos = (pos_x, pos_y)
            already = True
            if pos_x < 0 or pos_y < HEADER or pos_x >= HEIGTH or pos_y >= WIDTH:
                continue
            if self.grid.cell_state[(pos_x, pos_y)] == 1:
                continue
            for cue_node in self.cueList:
                if new_pos == cue_node.pos:
                    already = False
            for node in self.nodeList:
                if node.pos == new_pos and node.visited == False and already:
                    node.parent = current_node
                    self.cueList.append(node)
                            
        for node in self.nodeList:
            if node.visited:
                self.grid.cell_state[node.pos] = 6
        for node in self.cueList:
            if node.pos == self.end.pos:
                pass
            else:
                self.grid.cell_state[node.pos] = 4
        
        self.grid.cell_state[current_node.pos] = 5
    
    def stop(self):
        self.openList = []
        self.nodeList = []
        self.openList.append(self.start)
        for i in range(0, HEIGTH, SQUARE):
            for j in range(HEADER, WIDTH, SQUARE):
                if self.grid.cell_state[(i,j)] != 1:
                    self.grid.cell_state[(i,j)] = 0