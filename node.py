class Node:
    def __init__(self, pos=None, parent=None):
        self.parent = parent
        self.pos = pos
        
    def __str__(self):
        return str(self.pos)
    
    def __eq__(self, other):
        return self.pos == other.pos