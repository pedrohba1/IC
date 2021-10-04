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


# For each particle
#  Initialize particle
# End
# Repeat
#  For each particle
#  Calculate fitness value
#  If the fitness value is better than
# best fitness value (Pid) in history
#  Set current value as the new Pid
#  End
#  Choose the particle with the best
# fitness value of all the particles as
# the Pgd
#  For each particle
#   copy some individuals from Pgd and change them for the individuals in particle 
#   Run AG algorithm from this individuals
# according to equation (2)
#  End
# Until Stopping criteria

N = 10


ps = Particles(10, 6)

for 