import numpy as np
import networkx as nx
class Instance:
    def __init__(self, N):
        # constrói a instância do problema: seu grafo, com N^2 * N vertices, e suas N^2 * N
        boardArray = np.array([x+1 for x in range(N*N)])
        board = boardArray.reshape(N,N)
        print(board)
        Pij = 1/ N**4
        
        # construção do grafo em que os pesos são as probabilidades de transição
        G = nx.DiGraph()
        for fromNode in boardArray:
            for toNode in boardArray:    
                G.add_edge(fromNode, toNode, weight=Pij)
        
        
        # checar se a soma de todas as probabilidades de caminho deu 1
        acc = 0
        for u, v, weight in G.edges(data="weight"):
            acc += weight
        print(acc)        
        
        
        
        
        print(len(G.edges))