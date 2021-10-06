import numpy as np
from AG_Functions import gen_individuals, darwinize_individual
from Particle import Particle

class Particles:
    def __init__(self, N, n_queens):
        self.N = N
        self.board = np.array([x+1 for x in range(N*N)]).reshape(N,N)
        self.particles = [] 
        print('')
        for queens in gen_individuals(n_queens,N,10):
            score = darwinize_individual(queens, self.board)
            p = Particle(queens,score, self.board, self.N)
            self.particles.append(p)
        self.rank_particles_by_actual_score()
        self.max_particle = self.particles[0]


    # a ideia dessa função é sempre manter na lista de partículas uma ordem decrescente de score: 
    # a partícula de maior score atual está na posição 0 e a menor de todas na posição 100
    def rank_particles_by_actual_score(self):
        self.particles.sort(key=lambda p: p.actual_score , reverse=True)

    def rank_particles_by_hig_score(self):
        self.particles.sort(key=lambda p: p.high_score , reverse=True)

    def do_iteration(self):

        for particle in self.particles:
            particle.move_particle(self.max_particle)
            if particle.actual_score > self.max_particle.high_score:
                self.max_particle = particle

        print('score máximo atual', self.max_particle.high_score)        


