import numpy as np
import networkx as nx
from functions import fitness, get_distance_between, debug_board, dominated_set
from Queen import Queen
import random

class Instance:
    def __init__(self, N, N_queens):
        # deixei a inicialização de variáveis aqui para ficar mais fácil de ver quais existem
        self.N = N
        self.iterations = 0
        self.N_queens = N_queens
        self.queens = []
        self.board = []
        self.omega = 2
        self.alpha = 1.5
        self.beta = 1.5
        self.board_positions = []        
        self.board_positions = np.array([x+1 for x in range(N*N)])
        self.board = self.board_positions.reshape(N,N)
        self.best_queens = []
        self.best_fitness = 0
        
        # construção do grafo em que os pesos das arestas são o valor do feromônio (inicializa com 1)
        G = nx.DiGraph()
        for fromNode in self.board_positions:
            for toNode in self.board_positions:   
                distance = get_distance_between(fromNode, toNode, self.board)
                G.add_edge(fromNode, toNode, pheromone=1, distance=distance)
        

        # posiciona as N rainhas cada uma em um espaço do tabuleiro, sem que duas estejam na mesma posição
        # as rainhas são um objeto da classe Queen
        queens_positions = np.random.choice(self.board_positions,size=self.N_queens, replace=False)    
        for queen_position in queens_positions:
            self.queens.append(Queen(queen_position))
        self.G = G
        
    def show_best(self):
        print('melhor fitness', self.best_fitness)
        debug_board([queen.position for queen in self.best_queens], self.board)
    
    
    def do_tour(self):
        # zera os visitados de cada rainha porque é uma nova tour.
        # em cada tour as rainhas podem percorrer seu caminho livremente1
        for queen in self.queens:
            queen.clear_visited()
        
        ## faz N_queens iterações:
        for i in range(0, self.N_queens):
            self.do_iteration()
            
    def do_iteration(self):
        # a rainha (formiga) precisa andar para algum lugar.
        # antes dela andar, precisamos calcular o fitness para adicionar
        # ao feromônio e em seguida calcular as probabilidades de cada
        # caminho a ser tomado, com base na equação dada no artigo que leva em consideração feromônio e
        # distância 
        
        
        # print (len(fitness(self.queens, self.board)))
        # print(fitness(self.queens, self.board))
        # debug_board([queen.position for queen in self.queens], self.board)

        for queen in self.queens:
            ####### calcula o fitness e faz o ajuste nos feromônios
            
            S  = dominated_set([queen.position for queen in self.queens], self.board)
            actual_fitness = (len(S)/ (self.N**2))
            if actual_fitness > self.best_fitness:
                self.best_fitness = actual_fitness
                self.best_queens = self.queens

            print(actual_fitness)
            # print(queen.position)
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                if not queen.has_visited(to_node):
                    data['pheromone'] +=  data['pheromone'] + actual_fitness* self.omega
            ########
        
            
            ######## primeiro calcular as probabilidades:
            # cria o denominador do cálculo de probabilidade
            sum_non_visited = 0
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                if not queen.has_visited(to_node) and not to_node in set(queen.position for queen in self.queens):
                    sum_non_visited += (data['pheromone'] ** self.alpha)  * ((1 / data['distance']) ** self.beta)
            
            # cria o numerador e anexa ele como dado de um caminho, para cada caminho
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                if not queen.has_visited(to_node) and not to_node in set(queen.position for queen in self.queens):
                    self.G[from_node][to_node]['probability'] = (data['pheromone'] ** self.alpha)  * ((1 / data['distance']) ** self.beta) /sum_non_visited
                else: self.G[from_node][to_node]['probability'] = 0.0

            
            # ABAIXO FUNÇÃO PARA DEBUG
            # checa se a soma das probabilidades dá 1 ou beeem perto disso
            # sum_probs = 0
            # print('rainhas', [queen.position for queen in self.queens])
            # for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
            #     print('visitados da rainha', queen.visited)
            #     print('prob rainha sair de', from_node, ' e ir para', to_node , "{:.7f}".format(data['probability']))
            #     sum_probs += data['probability']
            # print(sum_probs) 
            ########

            ######## escolhe um caminho pra rainha             
            listed_edges = list(self.G.out_edges(queen.position, data=True))
            path_probs = []
            for _,_,data in listed_edges:
                path_probs.append(data['probability'])
                
            # escolhe um caminho com base na probabilidade dele e anda para o caminho
            chosen_path_index = np.random.choice(len(listed_edges), p=path_probs)
            chosen_path = listed_edges[chosen_path_index]
            # print(chosen_path)
            queen.set_position(chosen_path[1])
            queen.visit(chosen_path[1])
            ########
            
            ### faz a evaporação do feromônio citada no artigo:
            for (from_node, to_node ,data) in self.G.out_edges(queen.position, data=True):
                    data['pheromone'] = data['pheromone']*random.uniform(0,1)
                




        
        
        
