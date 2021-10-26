import numpy as np
import networkx as nx
from functions import fitness, get_distance_between
class Instance:
    def __init__(self, N, N_queens):
        # deixei a inicialização de variáveis aqui para ficar mais fácil de ver quais existem
        self.N = N
        self.iterations = 0
        self.N_queens = N_queens
        self.queens = []
        self.board = []
        
        
        # constrói a instância do problema: seu grafo, com N^2 * N vertices, e suas N^2 * N
        boardArray = np.array([x+1 for x in range(N*N)])
        self.board = boardArray.reshape(N,N)
        
        # construção do grafo em que os pesos das arestas são o valor do feromônio (inicializa com 1)
        G = nx.DiGraph()
        for fromNode in boardArray:
            for toNode in boardArray:   
                distance = get_distance_between(fromNode, toNode, self.board)
                G.add_edge(fromNode, toNode, pheromone=1, distance=distance)
        

        # posiciona as N rainhas cada uma em um espaço do tabuleiro, sem que duas estejam na mesma posição
        self.queens = np.random.choice(boardArray,size=N, replace=False)    
        self.G = G
    
    def do_iteration(self):
        
        # for u,v,a in self.G.edges(data=True):
        #     print (u,v,a)

        # a rainha (formiga) precisa andar para algum lugar.
        # antes dela andar, precisamos calcular as probabilidades de cada
        # caminho a ser tomado, com base na equação dada no artigo
        for (u,v,t) in self.G.out_edges(1, data=True):
            print(u,v,t)

        fitness(self.queens, self.board)




        
        
        
