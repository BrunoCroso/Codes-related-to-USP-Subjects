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
        - Foi utilizado o vídeo sugerido na descrição do EI

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não recebi ajuda externa 
'''

## ==================================================================
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas de tamanho mínimo, em ordem crescente,
        decrescente, etc.
    '''
    print("Testes do EI23 - ordenação por pivotação")
    
    
    testes = [[4],
              [4,9],
              [9,4],
              [1,2,3,4,5],
              [5,4,3,2,1],
              [5, 7, 4, 3, 8, 6],
              [6, 7, 5, 3, 8, 4],
              [99,33,55,77,11,22,88,66,33,44],
              [1,2,3,4,4,5,4,6,7,8,4],
              [1,2,3,4,5,6,7,7,6,5,4,3,64,2,1,6]]
    
    for i in testes:
        copia = i[:]
        n = pivote_seq(i)
        
        print(f'{copia} ---> {i}')
        print(f'Retorna {n}\n')
        

def pivote_seq(seq):
    ''' (list) -> int

    Recebe uma lista seq com n>0 elementos 
    e rearranja seus elementos para que o pivô, 
    o último elemento da lista,
    esteja na posição "ordenada" com relação aos demais 
    elementos, ou seja, todos os elementos menores fiquem
    a esquerda e todos os maiores fiquem a direita do pivô.

    Retorna um índice m tal que

        seq[:m] <= seq[m] < seq[m+1:]
    
    Exemplos:
    In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    In [3] m
    3
    In [4] seq
    [5, 4, 3, 6, 8, 7]

    ...

    In [11] seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    In [13] m
    1
    In [14] seq
    In [3, 4, 5, 6, 8, 7]

    DICAS:
    - observe que a pivotagem não ordena os elementos à 
    esquerda e à direita do pivô. Portanto, seu resultado
    pode ser diferente, desde que o pivô esteja na posição 
    correta.
    - não use sort() para resolver essa função, que tem 
    consumo de tempo O(n lg n). O consumo
    de tempo esperado para essa função é O(n) e o 
    de memória é O(1). 
    - O vídeo cujo link você encontra no enunciado dessa
    atividade ilustra uma possível solução.
    '''

    
    if len(seq) == 1:
        return 0

    if len(seq) == 2:
        if seq[0] > seq[1]:
            (seq[0], seq[1]) = (seq[1], seq[0])
            return 0
        else:
            return 1


    index_maior = 0
    index_menor = len(seq) - 2
    final = 0
    pivo = seq[len(seq)-1]
    
    while index_menor > index_maior:
        
        while seq[index_maior] <= pivo and index_maior < (len(seq) -1):
            index_maior += 1
            

        while seq[index_menor] > pivo and index_menor >= 0:
            index_menor -= 1
            
        if index_menor > index_maior:
            (seq[index_maior], seq[index_menor]) = (seq[index_menor], seq[index_maior])

        
        elif index_maior == index_menor:
            if seq[index_maior] > pivo:
                (seq[index_maior], seq[len(seq) - 1]) = (seq[len(seq) - 1], seq[index_maior])
                final = index_maior
                
            else:
                (seq[index_maior + 1], seq[len(seq) - 1]) = (seq[len(seq) - 1], seq[index_maior + 1])
                final = index_maior + 1
                
        else:
            (seq[index_maior], seq[len(seq) - 1]) = (seq[len(seq) - 1], seq[index_maior])
            final = index_maior

    return final



#-----------------------------------------------        
if __name__ == '__main__':
    main()

































