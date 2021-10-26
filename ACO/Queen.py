

class Queen:
    def __init__(self, position):
        self.position = position
        self.visited = set()
        self.visit(position)
        

    def visit(self, position):
        self.visited.add(position)
        
        
    def clear_visited(self):
        self.visited = set()
    
    def has_visited(self, position):
        return position in self.visited

    def set_position(self, position):
        self.position = position


        
        
        
