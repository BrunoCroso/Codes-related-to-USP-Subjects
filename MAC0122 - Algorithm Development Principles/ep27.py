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

## ==================================================================
#     Constantes que você pode usar em sua solução

DATAS = 365
SUCESSO = True
FRACASSO = False

## ==================================================================
# 
def main():
    '''
    Testes da classe Aniversario

    inclua mais 10 testes usando valores distintos de n e t.
    '''

    print("Testes do EI27 - Paradoxo do Aniversário")
    
    #Testes representam, pares (n, t)
    testes = [[0,0],
              [1,0],
              [0,1],
              [1,1],
              
              [10,20],
              [20,20],
              [50,20],
              [100,20],
              [500,20],
              
              [10,50],
              [10,100],
              [10,500],
              [10,10000],
              
              [40,100],
              [40,500],
              [40,2000],
              [40,10000]]
    
    for i in testes:
        print(f'\nPara n = {i[0]} e t = {i[1]}:')
        
        prob = Aniversario(i[0], i[1])
        print(f'Probabilidade = {prob}')
    
    print(30*'-')
    
    for i in range (10):
        print(f'n = {10*i} ---> Prob = {Aniversario(10*i, 100000)}')
        
## ==================================================================
# 
class Aniversario:

    #------------------------------------------
    def __init__(self, n, t):
        '''(Aniversario, int, int) -> None

        Recebe o número n de pessoas que podem entrar na sala
        e o número t de experimentos (trials). 
        Calcula a probabilidade de, ao selecionarmos n 
        datas uniformemente ao acaso, tenhamos
        duas datas iguais.
        '''        
        self.n = n
        self.t = t
        sucessos = 0
        
        for i in range(t):
            sucessos += self.experimento()
        
        if t == 0:
            self.p = 0
        else:
            self.p = sucessos/t    

    #------------------------------------------    
    def __str__(self):
        return str(self.p)

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' (Aniversario) -> bool

        Executa um experimento como descrito no enunciado,
        para uma sala com até 
        * self.n pessoas e 
        * self.t tentativas (trials)
        Retorna SUCESSO ou FRACASSO.

        DICA: para esse método, conjuntos são mais 
        eficientes que listas.
        '''
        if self.n == 0:
            return FRACASSO
        
        
        aniversarios = set()
        data = set()
        
        for i in range(self.n):
            
            data = set()
            valor = random.randrange(0,365)
            data.add(valor)

            
            if aniversarios.intersection(data) != set():
                return SUCESSO
            
            aniversarios.add(valor)
        
        
        return FRACASSO
        
        
        
        
        
        
        
        
        
        
        
        
        # implemente sua solução

## ==================================================================
# 
if __name__ == '__main__':
    main()