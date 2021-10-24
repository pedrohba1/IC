import numpy as np
import networkx as nx
class Instance:
    def __init__(self, N, N_queens):
        self.N = N
        self.iterations = 0
        self.N_queens = N_queens
        self.queens_positions = []
        
        # constrói a instância do problema: seu grafo, com N^2 * N vertices, e suas N^2 * N
        boardArray = np.array([x+1 for x in range(N*N)])
        board = boardArray.reshape(N,N)
        print(board)
        
        
        # construção do grafo em que os pesos das arestas são o valor do feromônio (inicializa com 1)
        G = nx.DiGraph()
        for fromNode in boardArray:
            for toNode in boardArray:    
                G.add_edge(fromNode, toNode, weight=1)
            
        # posiciona as N rainhas cada uma em um espaço do tabuleiro, sem que duas estejam na mesma posição
        self.queens_positions= np.random.choice(boardArray,size=N, replace=False)    
        self.G = G
    
     
     
        
        
    def do_iteration(self):

        
        
