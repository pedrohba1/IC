from AG_Functions import show_dominated_board


class Particle:
    def __init__(self, queens, score):
        
        # o melhor local não necessariamente é a posição atual da partícula
        # a posição dela é dada por suas rainhas:
        self.hs_queens = queens
        self.actual_queens = queens

        self.high_score = score
        self.actual_score = score

    def show_particle(self):        
        print("high sore", self.high_score)
        print("score atual", self.actual_score)
        print("tabuleiro atual:")
        show_dominated_board(self.actual_queens)
        print("tabuleiro do high score:")
        show_dominated_board(self.hs_queens)
