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


import time

def main():
    print('TESTE DE VELOCIDADES:\n')
    
    valores = [10, 20, 30, 40]
    
    for i in valores:
        print(f'Para n = {i}:')
        
        inicio = time.time()
        valorR =fibonacciR(i)
        fim = time.time()
        
        print(f'Tempo recursiva: {fim-inicio}')
        
        inicio = time.time()
        valorI = fibonacciI(i)
        fim = time.time()
        
        print(f'Tempo iterativa: {fim-inicio}')
        
        print(f'Resultados obtidos: {valorR} e {valorI}\n')
        



def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''
    
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    Fn = fibonacciR(n-2) + fibonacciR(n-1)
    
    return Fn
    

## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''

    if n == 0:
        return 0
    if n == 1:
        return 1

    Fn_menos_1 = 0
    Fn_menos_2 = 1
    Fn = 1
    
    for i in range(n):
        Fn = Fn_menos_1 + Fn_menos_2
        Fn_menos_2 = Fn_menos_1
        Fn_menos_1 = Fn
    
    return Fn

if __name__ == '__main__':
    main()

















