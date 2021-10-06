from Particles import Particles

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


# Gera as partículas
# Ordena elas pelo actual_score
# Substitui o high_score das sub50% pelo highscore das top50%
# aplica as seguintes substituições de velocidade
   #  substitui as rainhas atuais de cada partícula pelas rainhas do máximo local com probabilidade c1 de substituição
   #   substitui as rainhas atuais de cada partícula pelas rainhas de máximo global com probabilidade c2    
# repete o processo

N = 10
ps = Particles(10, 6)

for particle in ps.particles:
    print(particle.actual_score)



for i in range(0,1000):
    ps.do_iteration()
