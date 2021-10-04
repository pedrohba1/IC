import numpy as np
from AG_Functions import gen_individuals, get_fitness, show_dominated_board, darwinize_individual

class Particle:
    def __init__(self, N, n_queens):
        self.N = N
        self.board = np.array([x+1 for x in range(N*N)]).reshape(N,N)
        self.individuals = gen_individuals(n_queens,N,100)
        self.set_best_individual()

    def set_best_individual(self):
        fitness_values = get_fitness(self.individuals, self.board)
        self.best_fitness = fitness_values[np.argmax(fitness_values)][0]
        self.best_individual = self.individuals[np.argmax(fitness_values)]

    def show_best_individual(self):        
        print("valor de fitness do melhor indivíduo:", self.best_fitness)
        show_dominated_board(self.best_individual)


