from AG_Functions import show_dominated_board, darwinize_individual
import random
from random import seed


class Particle:
    def __init__(self, queens, score, board, N):
        
        # o melhor local não necessariamente é a posição atual da partícula
        # a posição dela é dada por suas rainhas:
        self.local_max_queens = queens
        self.actual_queens = queens
        self.board = board
        self.N = N

        self.high_score = score
        self.actual_score = score

        self.velocity = 1


    def convert_queen(self, queenInInt):
        if queenInInt <0: queenInInt = queenInInt*(-1)
        if queenInInt > self.N * self.N:
            queenInInt = queenInInt % (self.N*self.N)
            if queenInInt == 0: queenInInt +=1
            queenBin = format(queenInInt,'08b')
            return queenBin
        elif queenInInt == 0: 
            queenInInt += 1
            queenBin = format(queenInInt,'08b')
            return queenBin
        queenBin = format(queenInInt,'08b')
        return queenBin



    def move_particle(self, max_particle):
        # A velocidade vai ser aplicada em cada rainha.
        # primeiro usa a velocidade atual da partícula
        # a velocidade é recalculada para aquela rapinha
        queensInInt = []
        for queen in self.actual_queens:
            queensInInt.append(int(queen,2))  
        
        localMaxQueenInInt = []
        for max_queens in self.local_max_queens:
            localMaxQueenInInt.append(int(queen,2))
        
        maxParticleQueensInInt = []
        for max_queens in max_particle.local_max_queens:
            maxParticleQueensInInt.append(int(queen,2))

        w = 0.5
        c1 = 1.5   
        c2 = 2.5
        tmp_queens = []
        for idx, queen in enumerate(queensInInt):
            r1 = random.randint(1,4)    
            r2 = random.randint(1,4)

            self.velocity = w*self.velocity + c1*r1*(localMaxQueenInInt[idx] - queensInInt[idx]) + c2*r2*(maxParticleQueensInInt[idx] - queensInInt[idx])
            queensInInt[idx] = queensInInt[idx] + self.velocity
            queenInBin = self.convert_queen(int(queensInInt[idx]))
            tmp_queens.append(queenInBin)

           # print('rainhas no final', tmp_queens)
        new_score = darwinize_individual(tmp_queens, self.board)
        # print('score atual', self.actual_score)
        # print('máximo local', self.actual_score)
        # # print('novo score', new_score)
        self.actual_queens = tmp_queens
        self.actual_score = new_score
        if new_score > self.high_score:
            # print('novo score é maior que o highscore')
            self.local_max_queens = tmp_queens
            self.high_score = new_score




    def show_particle(self):        
        print("high sore", self.high_score)
        print("score atual", self.actual_score)
        print('rainhas atuais', self.actual_queens)
        print('rainahs do melhor tabuleiro', self.local_max_queens)
        print("tabuleiro atual:")
        show_dominated_board(self.actual_queens, self.N)
        print("tabuleiro do máximo local:")
        show_dominated_board(self.local_max_queens, self.N)
