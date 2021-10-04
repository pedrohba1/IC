
class Particle:
    def __init__(self, queens, score):
        self.queens = queens
        self.high_score = score
        self.actual_score = score