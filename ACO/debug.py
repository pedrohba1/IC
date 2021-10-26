from Queen import Queen
import numpy as np
from functions import fitness, get_distance_between, debug_board

N = 8
queens = [Queen(1), Queen(2)]
board_positions = np.array([x+1 for x in range(N*N)])
board = board_positions.reshape(N,N)
print('valor de fitness', len(fitness(queens, board)))
print(fitness(queens, board))
debug_board([queen.position for queen in queens], board)

