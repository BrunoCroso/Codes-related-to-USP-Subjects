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
        - Somente foi utilizado o texto indicado como leitura preliminar

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não recebi ajuda externa
'''

## ==================================================================

def main():

    print("Testes das suas funções recursivas \n")
    
    print('TESTES PARA MAXR:\n')
    print(f'maxR([12, 15, 7]) =\t{maxR([12, 15, 7])}')
    print(f'maxR([51]) =\t{maxR([51])}')
    print(f'maxR([]) =\t{maxR([])}')
    print(f'maxR([5,9,84,24,75,36,42]) =\t{maxR([5,9,84,24,75,36,42])}')

    print('\nTESTES PARA SOMAR:\n')
    print(f'somaR([12, -15, 7]) =\t{somaR([12, -15, 7])}')
    print(f'somaR([51]) =\t{somaR([51])}')
    print(f'somaR([]) =\t{somaR([])}')
    print(f'somaR([1,3,5,7,9]) =\t{somaR([1,3,5,7,9])}')
    print(f'somaR([-50,-20,-5,10,20,45]) =\t{somaR([])}')


## ------------------------------------------------------------------

def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplos: 
        - para a entrada [12, 15, 7], a funcao deve retornar 15.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar None.

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa max() do Python para resolver esse exercício.
    '''

    if lista == []:
        return None
    if len(lista) == 1:
        return lista[0]
    
    else:
        nova_lista = lista[:]
        if nova_lista[0] >= nova_lista[1]:
            del nova_lista[1]
        else:
            del nova_lista[0]
        return maxR(nova_lista)

## ------------------------------------------------------------------

def somaR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
        Exemplo: 
        - para a entrada [12, -15, 7], a funcao deve retornar 4.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar 0 (zero).

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa sum() do Python para resolver esse exercício.
    '''
    
    if lista == []:
        return 0
    if len(lista) == 1:
        return lista[0]
    
    else:
        nova_lista = lista[1:]
        return lista[0] + somaR(nova_lista)
    
## ------------------------------------------------------------------

if __name__ == '__main__':
    main()