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

    print("Testes da classe Array2d\n")

    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2d( (2,3), 1.7)   # criar Array2d com valor inicial 7
    print(f'teste 2: Criação do Array2d b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    print(f'teste 3: a[0,1] + 100 é: {a[0,1] + 100}') # acesso direto usando tupla: use o método __getitem__
    print()

    a[1,1] = -1    # atribuição usando tupla: use o método __setitem__
    print(f'teste 4: Array2d a:')
    print(a)


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''

        self.shape = shape
        self.size = shape[0]*shape[1]
        self.data = []
        for i in range (self.size):
            self.data += [val]

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        dado = self.data[(self.shape[1] * key[0]) + key[1]]
        return dado
        

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        
        posição = (self.shape[1] * key[0]) + key[1]
        self.data[posição] = valor
        return None

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        
        string = ''
        contador = 0
        for i in range (self.shape[0]):
            for c in range (self.shape[1]):
                if c == (self.shape[1]-1):
                    string += str(self.data[contador])
                    contador += 1
                else:
                    string += str(self.data[contador]) + ' '
                    contador += 1
            string += '\n'
        
        final = string[:(len(string)-1)]
        return final
    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar


## ==================================================================

if __name__ == '__main__':
    main()