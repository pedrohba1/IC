from Instance import Instance
from functions import dominated_set, debug_board

N = 8
N_queens = 5

instance = Instance(N, N_queens)


#fazer 10 tours. Cada tour mantém dados de feromônio da tour anterior
for i in range(0,200):
    instance.do_tour()


instance.show_best()

