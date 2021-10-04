import numpy as np
from AG_Functions import gen_individuals, darwinize_individual
from Particle import Particle

class Particles:
    def __init__(self, N, n_queens):
        self.N = N
        self.board = np.array([x+1 for x in range(N*N)]).reshape(N,N)
        self.particles = [] 
        print('')
        for queens in gen_individuals(n_queens,N,100):
            score = darwinize_individual(queens, self.board)
            p = Particle(queens,score)
            self.particles.append(p)
        self.rank_particles_by_actual_score()


    def rank_particles_by_actual_score(self):
        self.particles.sort(key=lambda p: p.actual_score , reverse=True)

