

class Queen:
    def __init__(self, position):
        self.position = position
        self.visited = set()
        self.visit(position)
        

    def visit(self, position):
        self.visited.add(position)
        
    def has_visited(self, position):
        return position in self.visited



        
        
        
