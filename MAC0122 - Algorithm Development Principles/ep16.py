# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Bruno Croso Cunha da Silva
    NUSP: 5524390

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

   - LISTA de fontes externas utilizadas (links ou referências como livros)
        - Não foi utilizada nenhuma fonte externa para este trabalho

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não recebi ajuda externa 
'''

import numpy as np
import time

## CONSTANTES

DEBUG = True

## ==================================================================

def main():
    
    global DEBUG
    DEBUG = False
    
    testes = [(0,0),(0,1),(3,2),(4,1),(6,3),(15,12),(28,20),(19,39)]
    
    print('TESTES:\n')
    
    for i in testes:
        inicioR = time.time()
        resultadoR = binomialR(i[0],i[1])
        fimR = time.time()
        tempoR = fimR - inicioR
        
        inicioI = time.time()
        resultadoI = binomialI(i[0],i[1])
        fimI = time.time()
        tempoI = fimI - inicioI
        
        print(f'Binomial{i}:')
        print('\t\t\tResultado\tTempo')
        print(f'Recursiva\t{resultadoR}\t\t\t{tempoR}')
        print(f'Iterativa\t{resultadoI}\t\t\t{tempoI}\n\n')
    
    DEBUG = True



## ==================================================================

def binomialI(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialI(3,2)  -> deve retornar 3
    b) binomialI(5,1)  -> deve retornar 5
    c) binomialI(1,5)  -> deve retornar 0
    d) binomialI(4,2)  -> deve retornar 6

    NOTA. Está função é iterativa.
    '''

    triangulo = np.zeros((n+1, k+1), int) 
    triangulo[:,0] = 1
    
    for linha in range (1,n+1):
        for coluna in range(1,k+1):
            if linha == coluna:
                triangulo[linha][coluna] = 1
            elif linha < coluna:
                triangulo[linha][coluna] = 0
            else:
                triangulo[linha][coluna] = triangulo[linha-1][coluna] + triangulo[linha-1][coluna-1]
                
    return triangulo[n][k]

## ==================================================================

def binomialR(n, k):
    '''(int,int) -> int

    RECEBE inteiros não-negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialR(3,2)  -> deve retornar 3
    b) binomialR(5,1)  -> deve retornar 5
    c) binomialR(1,5)  -> deve retornar 0
    d) binomialR(4,2)  -> deve retornar 6

    NOTA. Está função é uma interface para a função 
          binomialRM() e não deve ser alterada.
    '''
    # cria um array de dimensão (n+1)x(k+1) para ser usado como rascunho
    rascunho = np.zeros((n+1, k+1), int) 
    rascunho[:,0] = 1

    bin = binomialRM(n, k, rascunho)
    if DEBUG:
        print("Debug ligado.")
        print(f"bin({n}, {k}) = {bin}")
        print(f"   Rascunho:\n{rascunho}")

    return bin

## ==================================================================

def binomialRM(n, k, rascunho):
    '''(int, int, array) -> int

    RECEBE inteiros não negativos n e k e um array bidimensional rascunho.
    RETORNA o valor de binomial(n,k).

    NOTA. Está função é recursiva.
        Ela usa as posições do array rascunho para  guardar os valores dos 
        binomiais já calculado: 
           - rascunho[i][j] armazenará o valor de binomial(i, j).
        Com isso a função evita que um mesmo número binomial seja recalculado 
        várias vezes.
    '''
    
    if k == n:
        rascunho[n][k] = 1
    
    elif n < k:
        rascunho[n][k] = 0
    
    else:
        if rascunho[n-1][k] == 0 and n != k:
            rascunho[n-1][k] = binomialRM(n-1, k, rascunho)
        
        if rascunho[n-1][k-1] == 0:
            rascunho[n-1][k-1] = binomialRM(n-1, k-1, rascunho)
            
        rascunho[n][k] = rascunho[n-1][k] + rascunho[n-1][k-1]      
    
    
    return rascunho[n][k]
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
