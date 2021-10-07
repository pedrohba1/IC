from Particles import Particles
import time

# The information
# sharing mechanism in PSO is significantly
# different. In GAs, chromosomes share
# information with each other. So the whole
# population moves like a one group towards an
# optimal area. In PSO, only best neighborhood
# gives out the information to others. It is a one
# way information sharing mechanism. The
# evolution only looks for the best solution. All
# the particles tend to converge to the best
# solution quickly even in the local version in
# most cases.


start  = time.time()
ps = Particles(11,7)
for i in range(0,1000):
    # ps.rank_particles_by_hig_score()
    # print('ranking das partículas')
    # for particle in ps.particles:
    #     print(particle.high_score)
    ps.do_iteration()


ps.rank_particles_by_hig_score()
ps.particles[0].show_particle()
end = time.time()
print('tempo de execução total', (end - start))

