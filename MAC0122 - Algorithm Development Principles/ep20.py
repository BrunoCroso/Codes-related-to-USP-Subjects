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

import random

def main():
    '''
        Testes das suas funções
    '''
    
    print('Testes da função "insira_ultimo(seq, n)" \n')

    testes = [[4, 7, 11, 5, 3], [4, 7, 11, 5, 3], [4, 5, 7, 11, 3]]
    enes = [3, 4, 5]

    for i in range(len(testes)):
        antes = testes[i][:]
        insira_ultimo(testes[i],enes[i])
        print(f'Para n = {enes[i]}: {antes} ----> {testes[i]} \n')


    print('\n\nTestes da função "ordene_por_insercao(seq)" \n')
        
    for i in range(6):
        
        teste = []
        for c in range(7):
            elemento = random.randint(1,10)
            teste.append(elemento)
            
        antes = teste[:]
        ordene_por_insercao(teste)
        
        print(f'{antes} ----> {teste}')
        
        antes.sort()
        if teste == (antes):
            print('CORRETO \n')


## ==================================================================

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    Essa função é a base para o algoritmo de ordenação 
    por inserção, que veremos em uma próxima aula e 
    não se trata de um algoritmo completo de ordenação.

    Essa função considerar apenas a porção da lista seq 
    no intervalo [0:n].

    A ideia é visitar cada elemento, a partir do fim da 
    porção, ou seja, do elemento de índice n-1.
    Caso o elemento anterior seja maior, os elementos são
    trocados de posição, fazendo o elemento visitado "descer"
    na lista. A varredura deve persistir enquanto o elemento 
    visitado for menor que o seu anterior.

    Por exemplo,  para seq = [4, 7, 11, 5, 3] e n = 3 a
    função não precisa fazer nada pois o elemento anterior
    ao 11 já é menor. 

    Para seq = [4, 7, 11, 5, 3] e n = 4 a
    função deve deslocar o 5 até que seq se torne 
    [4, 5, 7, 11, 3]. 

    Outro exemplo, para seq = [4, 5, 7, 11, 3] e n = 5 a
    função deve deslocar o 3 até que seq se torne 
    [3, 4, 5, 7, 11]. 

    DICA: não use outras listas, nem fatias. Basta
    varrer seq, comparar com seu vizinho anterior
    e trocar enquanto necessário.

    '''

    parada = False
    posição = n-1
    
    while parada == False and posição > 0:
        if seq[posição] < seq[posição - 1]:
            (seq[posição], seq[posição-1]) = (seq[posição-1], seq[posição])
        else:
            parada = True
        
        posição -= 1
    
## ==================================================================

def ordene_por_insercao(seq):
    ''' (list) -> None

    A ideia de ordenação por inserção (insertion sort)
    é considerar porções da lista, a partir de 2 elementos até n.
    Para cada porção, apenas o último elemento precisa ser 
    deslocado até sua posição correta.

    Exemplo para a lista [4, 7, 5, 3]
    - inicio com a porção da lista de tamanho 2 contendo [4, 7, ? , ?]. 
        O último elemento já está na posição correta. 
    - a ordenação continua com a porção de tamanho 3 com [4, 7, 5, ?]
        O último elemento da porção, o 5, precisa ser deslocado até
        sua posição final [4, 5, 7, ?]
    - a ordenação continua com a porção de tamanho 4, agora com 
        [4, 5, 7, 3]. O último elemento da porção, o 3, precisa ser
        deslocado até sua posição final [3, 4, 5, 7].
    - fim, pois já tratamos todas as porções até o tamanho n.

    O que você deve fazer: 

    A função recebe uma sequência de números em ordem aleatória. 
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por inserção.

    Essa função DEVE usar a função insira_ultimo().


    '''
    
    for i in range(len(seq) -1):
        insira_ultimo(seq, i+2)
    
    
    
    # escreva sua solução

## ==================================================================
## Escreva outras coisas que desejar
## ==================================================================


## ==================================================================

if __name__ == '__main__':
    main()

## ==================================================================
