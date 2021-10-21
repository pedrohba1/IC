import numpy as np

class Instance:
    def __init__(self, N):
        # constrói a instância do problema: seu grafo, com N^2 * N vertices, e suas N^2 * N
        boardArray = np.array([x+1 for x in range(N*N)])
        board = boardArray.reshape(N,N)
        print(board)
        Pij = 1/64
