import numpy as np
from settings import *

class AStar:
    def __init__(self, grid):
        self.openList = []
        self.closedList = []
        self.start = Node(grid.start)
        self.end = Node(grid.end)
        self.openList.append(self.start)
        self.grid = grid
    def run(self):
        if len(self.openList) == 0:
            self.path = []
            return True
        current_node = self.openList[0]
        current_index = 0
        for index, item in enumerate(self.openList):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        self.openList.pop(current_index)
        self.closedList.append(current_node)
        

        if current_node == self.end:
            self.path = []
            current = current_node
            while current is not None:
                self.path.append(current.pos)
                current = current.parent
            return True

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            pos_x = current_node.pos[0] + SQUARE * new_position[0]
            pos_y = current_node.pos[1] + SQUARE * new_position[1]
            new_pos = (pos_x, pos_y)
            if pos_x < 0 or pos_y < 0 or pos_x >= HEIGTH or pos_y >= WIDTH:
                continue
            if self.grid.cell_state[(pos_x, pos_y)] == 1:
                continue
            new_node = Node(new_pos, current_node)
            children.append(new_node)

        for child in children:
            is_closed = False
            for closed_child in self.closedList:
                if child == closed_child:
                    is_closed = True
            
            if not is_closed:
                child.g = int(np.sqrt(((child.pos[0] - self.start.pos[0]) ** 2) + ((child.pos[1] - self.start.pos[1]) ** 2)))
                child.h = int(np.sqrt(((child.pos[0] - self.end.pos[0]) ** 2) + ((child.pos[1] - self.end.pos[1]) ** 2)))
                child.f = child.g + child.h
                is_opened = False
                for index, open_node in enumerate(self.openList):
                    if child == open_node and child.g >= open_node.g:
                        is_opened = True
                if not is_opened:
                    self.openList.append(child)

        for node in self.closedList:
            self.grid.cell_state[node.pos] = 6
        for node in self.openList:
            self.grid.cell_state[node.pos] = 4
        self.grid.cell_state[current_node.pos] = 5
        return False

    def state(self):
        print('='*40)
        # print(self.path)
        for item in self.openList:
            print(item, '==>', item.g, item.h)
        for item in self.closedList:
            print(item)

class Node:
    def __init__(self, pos=None, parent=None):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def __str__(self):
        return str(self.pos)
    
    def __eq__(self, other):
        return self.pos == other.pos
        