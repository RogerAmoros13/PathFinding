from platform import node
from settings import *
from node import Node
import numpy as np

class Node_D(Node):
    def __init__(self, pos=None, parent=None):
        Node.__init__(self, pos, parent)
        self.dist = -1
        self.visited = False
    
    def __gt__(self, node1):
        return self.dist > node1.dist

    def __lt__(self, node1):
        return self.dist < node1.dist
    
    def __bool__(self):
        if self.visited:
            return True
        return False

class Dijsktra:
    def __init__(self, grid):
        self.cueList = []
        self.nodeList = []
        self.grid = grid
        for i in range(0, HEIGTH, SQUARE):
            for j in range(0, WIDTH, SQUARE):
                node = Node_D((i, j))
                if (i, j) == grid.start:
                    node.dist = 0
                    self.cueList.append(node)
                self.nodeList.append(node)
        self.end = Node_D(self.grid.end)
        self.path = []
    
    def run(self):
        if len(self.cueList) == 0:
            return True
        
        current_node = self.cueList[0]
        current_index = 0
        for index, node in enumerate(self.cueList):
            if node < current_node and node != -1:
                current_node = node
                current_index = index
        current_node.visited = True
        self.cueList.pop(current_index)
        if current_node == self.end:
            self.path = []
            current = current_node
            while current is not None:
                self.path.append(current.pos)
                current = current.parent
            return True

        adjacent_list = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_pos = (current_node.pos[0] + SQUARE * new_position[0], current_node.pos[1] + SQUARE * new_position[1])
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= WIDTH or new_pos[1] >= HEIGTH:
                continue
            if self.grid.cell_state[new_pos] == 1:
                continue
            
            for node in self.nodeList:
                if node.pos == new_pos:
                    adjacent_list.append(node)
        for adjacent in adjacent_list:
            # print(adjacent.visited)
            if adjacent.visited:
                pass
            else:
                if adjacent.dist == -1 or adjacent.dist > current_node.dist + 1:
                    if adjacent.dist == -1:
                        adjacent.dist = 1
                    else:
                        adjacent.dist = current_node.dist + 1
                    adjacent.parent = current_node
                    self.cueList.append(adjacent)                    

                
        for node in self.nodeList:
            if node.visited:
                self.grid.cell_state[node.pos] = 6
        for node in self.cueList:
            self.grid.cell_state[node.pos] = 4
        
        self.grid.cell_state[current_node.pos] = 5
        # for node in self.nodeList:
        #     if node.visited == True:
        #         print(node)
        #         print('recontrarepolla')
        
        return False
            