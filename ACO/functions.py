import numpy as np
from math import sqrt

# A função abaixo retornar o fitness, que é um valor de 0 ao número de rainhas (Nq).
# O fitness, nesse caso, é dado pelo número de posições no tabuleiro nas quais
# as raihas posicionadas neles não estarão atacando nenhuma outra. Ou seja, é a
# restrição do jogo
# O ideal é encontrar as Nq posições de forma que nenhuma das rainhas se ataquem,
# então quando mais próximo de N o valor, melhor.

def fitness(queens, board, verbose=True):
    queens_positions_set = set()
    for queen in queens:
        queens_positions_set.add(queen.position)
    
    satisfying_positions = set()
    diags = get_all_diags(board)
    all_positions = board.flatten()
    for checking_position in all_positions:
        is_valid = check_position_validity(board,checking_position, queens_positions_set)        
        if (is_valid):
            satisfying_positions.add(checking_position)
    return satisfying_positions
    


def check_position_validity(board, checking_position, queens_positions_set):
    coordinates = np.where(board == checking_position)
    i = coordinates[0][0]
    j = coordinates[1][0]
    row = board[i,:]
    column = board[j,:]
    position_diags = get_diags_containing_position(board, checking_position)
    for position in row: 
        if (position in queens_positions_set):
            return False
    for position in column:
        if (position in queens_positions_set):
            return False
    for diag in position_diags:
        for position in diag:
            if (position in queens_positions_set):
                return False

    return True
             
            
def get_all_diags(board):
    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1])]
    diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1))
    return [n.tolist() for n in diags]



def get_diags_containing_position(board, position):
    diags = get_all_diags(board)
    valid_diags = []
    for diag in diags:
        if position in set(diag):
            valid_diags.append(diag)
    return valid_diags

def debug_board(queens,board):
    N = board.shape[0]
    arr =  [x+1 for x in range(N*N)]
    print('tabuleiro comum')
    print(board)
    

    dominated = dominated_set(queens, board)
    for dominated_pos in list(dominated):
        arr[dominated_pos-1] = 'D'

    for queen in queens:
        arr[queen-1] = 'r'
    
    
    
    axu_board = np.array(arr)
    axu_board = axu_board.reshape(N,N)
    print('tabuleiro de dominações e rainhas')
    print(axu_board)
    

    
              
# para não ter que fazer breadth-frist search e complicar demais, 
def get_distance_between(position1, position2, board):
    coord1 = np.where(board == position1)
    i1 = coord1[0][0]
    j1 = coord1[1][0]
    
    coord2 = np.where(board == position2)
    i2 = coord2[0][0]
    j2 = coord2[1][0]

    distance =  sqrt((i1 -i2)**2 + (j1 - j2)**2)
    if (distance == 0): distance = 1.0
    return distance

def dominated_set(queens, chessBoard, verbose=False):
    S = set()
    N = chessBoard.shape[0]

    if verbose:
        print('tabuleiro que chega no dominatedSet')
        print(chessBoard)
    
    for queen in queens:
        queenBox = queen
        queenPosition = np.where(chessBoard == queenBox)
        i = queenPosition[0][0]
        j = queenPosition[1][0]
        if verbose: 
            print("posição matricial: (", i,j, ")" , 'valor: ', queenBox)

        if(verbose):
            # quadrados dominados na horizontal:
            print(chessBoard[i,:])
            # quadrados dominados na vertical:
            print(chessBoard[:,j])
       
        S.update(chessBoard[i,:])
        S.update(chessBoard[:,j])
        for d in range(-N+1,N):
             # diagonal
            diag = chessBoard.diagonal(d)
            # diagonal invertida
            invertDiag = np.fliplr(chessBoard).diagonal(d)
            if queenBox in diag:
                if verbose:
                    print(diag)
                S.update(diag)
            if queenBox in invertDiag:
                if verbose:
                    print(invertDiag)
                S.update(invertDiag)
    return S





