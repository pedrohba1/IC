import numpy as np
import networkx as nx
from functions import fitness, get_distance_between
from Queen import Queen
class Instance:
    def __init__(self, N, N_queens):
        # deixei a inicialização de variáveis aqui para ficar mais fácil de ver quais existem
        self.N = N
        self.iterations = 0
        self.N_queens = N_queens
        self.queens = []
        self.board = []
        self.board_positions = []
        
        # constrói a instância do problema: seu grafo, com N^2 * N vertices, e suas N^2 * N
        self.board_positions = np.array([x+1 for x in range(N*N)])
        self.board = self.board_positions.reshape(N,N)
        print(self.board)
        # construção do grafo em que os pesos das arestas são o valor do feromônio (inicializa com 1)
        G = nx.DiGraph()
        for fromNode in self.board_positions:
            for toNode in self.board_positions:   
                distance = get_distance_between(fromNode, toNode, self.board)
                G.add_edge(fromNode, toNode, pheromone=1, distance=distance)
        

        # posiciona as N rainhas cada uma em um espaço do tabuleiro, sem que duas estejam na mesma posição
        # as rainhas são um objeto da classe Queen
        queens_positions = np.random.choice(self.board_positions,size=N, replace=False)    
        for queen_position in queens_positions:
            self.queens.append(Queen(queen_position))
        self.G = G
    
    def do_iteration(self):
        
        # for u,v,a in self.G.edges(data=True):
        #     print (u,v,a)

        # a rainha (formiga) precisa andar para algum lugar.
        # antes dela andar, precisamos calcular as probabilidades de cada
        # caminho a ser tomado, com base na equação dada no artigo
        
        
        
        for queen in self.queens:
            sum_non_visited = 0
            # cria o denominador do cálculo de probabilidade
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                if not queen.has_visited(to_node):
                    sum_non_visited += data['pheromone'] * (1 / data['distance'])
            
            #cria o numerador e anexa ele como dado de um caminho, para cada caminho
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                if queen.has_visited(to_node):
                    self.G[from_node][to_node]['probabilty'] = 0
                else: self.G[from_node][to_node]['probabilty'] = data['pheromone'] * (1 / data['distance'])
                
            
            sum_probs = 0
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                print(from_node, to_node, data)
                sum_probs += data['probabilty']
        
            print(sum_probs)
            print(sum_non_visited)
            
        
        
        
        
            
                
        fitness(self.queens, self.board)




        
        
        
