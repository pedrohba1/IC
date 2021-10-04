from Particle import Particle

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

p = Particle(10, 6)
p.show_best_individual()