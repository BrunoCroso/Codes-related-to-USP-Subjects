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

## ==================================================================
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Testes do EI22 - ordenação por intercalação")

    testes = [[[],[]],
              [[7],[]],
              [[],[14]],
              [[1],[6]],
              [[8],[4]],
              [[1,9],[5]],
              [[12],[1,3]],
              [[1,3,5,7,9],[2,4,6,8,10]],
              [[1,1,1],[1,1,8]],
              [[1,3,5,6,8,9,14],[5,6,7]],
              [[-15,-10,-2,5,9,72,555],[-400,-20,-14,-9,-8,13,1579646]]]
    
    for i in testes:
        nova_lista = intercale_seqs(i[0], i[1])
        print(f'{i[0]} e {i[1]} ---> {nova_lista} \n')

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

    Recebe seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos
        
    Retorna uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    Exemplo para 
        seq1 = [7, 11, 56] e 
        seq2 = [-5, 7, 99, 104]
    
    a função deve retornar a lista:
        [-5, 7, 7, 11, 56, 99, 104]
    '''


    n1 = len(seq1)
    n2 = len(seq2)
    
    index_1 = 0
    index_2 = 0
    final = []
    
    for i in range(n1 + n2):
        
        if index_1 == n1:
            final.append(seq2[index_2])
            index_2 += 1
        
        elif index_2 == n2:
            final.append(seq1[index_1])
            index_1 += 1
        
        elif seq1[index_1] <= seq2[index_2]:
            final.append(seq1[index_1])
            index_1 += 1
        
        elif seq1[index_1] > seq2[index_2]:
            final.append(seq2[index_2])
            index_2 += 1
    
    return final


#--------------------------------------------
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    