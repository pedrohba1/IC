import numpy as np
from random import seed
from random import randint

N = 10


def dominatedSet(queens, chessBoard, verbose=False):
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


def gen_individuals(N_queens, N, N_individuals, verbose=True): 
    print('')
    A = np.empty((1,N_queens), dtype='str')
    for i in range (0,N_individuals):
        newRow = []
        for j in range (0,N_queens):
            randVal = randint(1,N*N)
            randInBin = format(randVal,'08b')
            while randInBin in newRow: 
                randVal = randint(1,N*N)
                randInBin = format(randVal,'08b')
            newRow.append(randInBin)
        A = np.vstack([A, newRow])
    # apaga a primeira linha que é gerada na inicialização da matriz
    A = np.delete(A,0, 0)
    return A


def darwinize_individual(ind, chessBoard):
    indInInteger = []
    N = chessBoard.shape[0]
    for queen in ind:
        inIntQueen = int(queen,2)
        indInInteger.append(inIntQueen)
    S = dominatedSet(indInInteger, chessBoard, verbose=False)
    ## o jeito de calcular o fitness como foi dito anteriormente
    return len(S)/ (N*N) 



def getFitness(population, chessBoard, verbose=False):
    fitness_values = np.empty((1), dtype='int64')
    for indi in population:
        if verbose: print('individo no getFitness', indi)
        fit = darwinize_individual(indi, chessBoard)
        fitness_values = np.vstack([fitness_values, fit])
    fitness_values = np.delete(fitness_values,0, 0)
    return fitness_values



def moreAdapted(population, chessBoard):
    n_queens = population.shape[1]
    fitness_values = getFitness(population, chessBoard)

    # Selecionará os 50% individuos com maior fitness_values
    n_ind = len(population)
    individuals = np.empty((1,n_queens), dtype='str')
    fit = np.empty((1), dtype='str')

    for i in range(n_ind):
        max_fitness_idx = np.argmax(fitness_values)
        fit = np.vstack([fit,fitness_values[max_fitness_idx]])
        individuals = np.vstack([individuals, population[max_fitness_idx]])
        fitness_values[max_fitness_idx] = -99999999999
    individuals = np.delete(individuals,0, 0)
    fit = np.delete(fit,0,0)
    individuals = individuals[0:int(n_ind/2)]
    fit = fit[0:int(n_ind/2)]
    return individuals


def roulette_wheel(population, chessBoard):
    fitness_values = getFitness(population, chessBoard)

    y = fitness_values.astype(np.float)
    Soma = np.sum(y)
    Prob_escolhido = np.empty((1), dtype='float')
  
    for i in y:   
        Prob_escolhido = np.vstack([Prob_escolhido, i/Soma])
    Prob_escolhido = np.delete(Prob_escolhido,0,0) 
    Prob_escolhido = np.transpose(Prob_escolhido) 
    indices = np.random.choice(len(population),size= 2 ,p=Prob_escolhido.flatten())
    ind = population[indices]
    return ind


def validate_dna(dna, verbose=False):
    # N é variaǘel global, tome cuidado
    if verbose: 
        print('valida o dna')
        print('dimensão', N)
    dnaInInt = int(dna,2)
    
    if verbose: print('valor anterior: ', dnaInInt)
    if dnaInInt > N*N:
        dnaInInt = dnaInInt % (N*N)
        if dnaInInt == 0: dnaInInt +=1
        dna = format(dnaInInt,'08b')
        if verbose: print('valor após validação: ', dnaInInt)
        return dna
    elif dnaInInt == 0: 
        dnaInInt += 1
        dna = format(dnaInInt,'08b')
        return dna
    else: return dna    


def crossover(parents, verbose=False):
    DNA_SIZE = 8
    individual1 = parents[0]
    individual2 =  parents[1]
    n_queens = individual1.shape[0]
    crossedIndividuals = np.empty((1,n_queens), dtype='str')
    if verbose: print('pais', parents)
    DNA1 = []
    DNA2 = []
    for i in range(0, n_queens):
        pos = randint(1, DNA_SIZE-1)
        if verbose: print('posição de troca: ', pos)
        dna1=individual1[i]
        dna2=individual2[i]
        generated1, generated2 = (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])
        generated1 = validate_dna(generated1)
        DNA1.append(generated1)
        generated2 = validate_dna(generated2)
        DNA2.append(generated2)
    crossedIndividuals = np.vstack([crossedIndividuals, [DNA1, DNA2]])
    crossedIndividuals = np.delete(crossedIndividuals,0, 0)
    return crossedIndividuals



def mutate(individual, verbose=False, debug=False):
    DNA_SIZE = 8
    top = 100
    if debug: top = 1
    if(randint(1,top) <= 5):
        mutatedIndividual =[]
        for DNA in individual:
                if verbose: print('antes da mutação', DNA)
                DNA = list(DNA)
                # pode acontecer de mudar a mesma posição duas vezes. Acho que não tem problema
                pos1 = randint(0, DNA_SIZE-1)
                pos2 =  randint(0, DNA_SIZE-1)
                if verbose: print('mudou as posições:', pos1, pos2)
                if DNA[pos1] == "1": DNA[pos1] = "0"
                elif DNA[pos1] == "0": DNA[pos1] = "1"
                if DNA[pos2] == "1": DNA[pos2] = "0"
                elif DNA[pos2] == "0": DNA[pos2] = "1" 
                DNAinString = "".join(DNA)
                DNA = validate_dna(DNAinString)
                mutatedIndividual.append(DNA)
        if verbose: print('após a mutação', mutatedIndividual)
        return mutatedIndividual 
    else:
        return individual            


def do_iterations(n_iters, n_queens, chessBoard_dimension):
    # constrói o tabuleiro
    N = chessBoard_dimension
    chessBoard = np.array([x+1 for x in range(N*N)])
    chessBoard = chessBoard.reshape(N,N)

    # gera os primeiros 100 indivíduos:
    A = gen_individuals(n_queens,N,100)
    i = 1
    while i <= n_iters:
        # já filtra o top 50%
        A = moreAdapted(A, chessBoard)  
        
        # vamos gerar mais 50 indivíduos à partir de 25 pares selecionados de pares com a roleta, e esses pares vão 
        # gerar dois indivíduos cada um. No final temos 100 indivídus.
        parentsSelected = []
        for j in range (0,25):
            parents = roulette_wheel(A, chessBoard)
            parentsSelected.append(parents)
        
        # agora fazemos os pais cruzarem. Cada pai vai gerar um par de filhos.
        childrenCreated = []
        for parents in parentsSelected:
            children = crossover(parents)
            childrenCreated.append(children)

        # aplica a mutação nos filhos, com base na chance de 5% definida na função
        for idx, children in enumerate(childrenCreated):
            childrenCreated[idx][0] = mutate(children[0])
            childrenCreated[idx][1] = mutate(children[1])

        # separar os pares e alocá-los numa matriz:
        AllIndividuals = np.empty((1,n_queens), dtype='str')
        for k in range(0, len(childrenCreated)):
            AllIndividuals = np.vstack(([ AllIndividuals, childrenCreated[k][0]]))
            AllIndividuals = np.vstack(([ AllIndividuals, childrenCreated[k][1]]))
            AllIndividuals = np.vstack(([ AllIndividuals, parentsSelected[k][0]]))
            AllIndividuals = np.vstack(([ AllIndividuals, parentsSelected[k][1]]))
        AllIndividuals = np.delete(AllIndividuals,0, 0)


        fitness_values = getFitness(AllIndividuals, chessBoard)
        A = AllIndividuals
        
        print('melhor indivíduo da iteração', i,' :' , fitness_values[np.argmax(fitness_values)])
        print('posição das rainhas do melhor individuo',A[np.argmax(fitness_values)])
        i += 1
    return 1