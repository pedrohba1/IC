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
        self.c1 = 0.2
        self.c2 = 0.4

        self.high_score = score
        self.actual_score = score

        self.velocity = 1


    def move_particle(self, max_particle):
    # a velocidade é simplesmente o array do máximo local e do máximo global
    # é feita uma iteração nas rainhas da partícula. 
    # a cada iteração a rainha na posição i tem chance c1 de ser trocada por uma rainha do máximo global
    # na mesma iteração, a rainha na posição i tem chance c2 de ser trocada por uam rainha do máximo local
    # A rainha só pode ser trocada por uma no máximo global ou por uma no máximo global. Pode acontecer também
    # de não haver trocas
        # print('rainhas atuais', self.actual_queens)
        # print('rainhas do máximo local', self.local_max_queens)
        # print('rainhas do máximo global', max_particle.local_max_queens)
        # print('score do máximo global', max_particle.actual_score)
        # print('fitness da rainha antes', self.actual_score)

        tmp_queens = self.actual_queens
        for idx, queen in enumerate(self.actual_queens):
            if random.random() < self.c2:
                tmp_queens[idx] = self.local_max_queens[idx]
            elif random.random() < self.c1:
                tmp_queens[idx] = max_particle.local_max_queens[idx]
        
        # print('rainhas no final', tmp_queens)
        new_score = darwinize_individual(tmp_queens, self.board)
        # print('score atual', self.actual_score)
        # print('máximo local', self.actual_score)
        # print('novo score', new_score)
        self.actual_queens = tmp_queens
        self.actual_score = new_score
        if new_score > self.high_score:
            # print('novo score é maior que o highscore')
            self.local_max_queens = tmp_queens
            self.high_score = new_score
        # print('fitness da rainha no final', new_score)
        # print('fitness do máximo global', max_particle.actual_score)





    def show_particle(self):        
        print("high sore", self.high_score)
        print("score atual", self.actual_score)
        print('rainhas atuais', self.actual_queens)
        print('rainahs do melhor tabuleiro', self.local_max_queens)
        print("tabuleiro atual:")
        show_dominated_board(self.actual_queens, self.N)
        print("tabuleiro do máximo local:")
        show_dominated_board(self.local_max_queens, self.N)
