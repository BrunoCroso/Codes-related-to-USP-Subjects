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

    print("Testes da classe Array2d e comparação com Numpy\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a) como no EG10
    a.resize( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.resize( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'linha a.getlin(0)\n{linha}\n')

    coluna = b.getcol(1)
    print(f'coluna b.getcol(1)\n{coluna}\n')

    print(f'linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')
    
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
    def resize(self,tupla):
        '''(Array2d, tuple) -> None
        
        Recebe o próprio objeto e uma tupla com dimensões e modifica o objeto
        para ter estas dimensões.
        '''
        
        self.shape = tupla
        
        
        
    # ---------------------------------------------------------------
    def copy(self):
        '''(Array2d) -> Array2d
        
        Ao ser chamada, retorna uma cópia (clone) do objeto
        '''
        
        copia_shape = self.shape[:]
        copia = Array2d(copia_shape, 0)
        copia.data = self.data[:]
        return copia


    # ---------------------------------------------------------------
    def reshape(self,dimensões):
        '''(Array2d,tuple) -> Array2d
        
        Recebe o prório objeto e uma tupla com dimensões e retorna uma vista do 
        Array2d inicial (compartilhando a mesma lista data).
        '''
        vista_shape = dimensões
        vista = Array2d(vista_shape, 0)
        vista.data = self.data
        return vista
    
    # ---------------------------------------------------------------
    def getlin(self, lin):    
        '''(Array2d,int) -> Array2d
        
        Recebe o prório objeto e um inteiro lin e retorrna um Array2d que contem a 
        línha de índice lin do objeto.
        '''
        
        shape = self.shape
        inicial = lin * shape[1]
        novo = Array2d((1,shape[1]),0)
        cont = 0
        for i in range(inicial, inicial + shape[1]):
            novo.data[cont] = self.data[i]
            cont += 1
        
        return novo
        
        
    
    # ---------------------------------------------------------------
    def getcol(self, col):
        '''(Array2d,int) -> Array2d
 
        Recebe o prório objeto e um inteiro col e retorrna um Array2d que contem a 
        coluna de índice col do objeto.
        '''
        
        shape = self.shape
        inicial = col
        novo = Array2d((shape[0],1),0)
        cont = 0
        for i in range(inicial,self.size,shape[1]):
            novo.data[cont] = self.data[i]
            cont += 1
            
        return novo

    # ---------------------------------------------------------------
    def dot(self, other): 
        '''(Array2d,Array2d) -> (int or float)
        
        Recebe o prório objeto e um Array2d other e retorna um escalar resultante
        do produto termo a termo entre o objeto e other.
        '''
        
        soma = 0
        for i in range(self.size):
            multiplicados = self.data[i] * other.data[i]
            soma += multiplicados

        return soma
        
    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar

def matmul( esq, dir ):
    '''(Array2d,Array2d) -> Array2d
    
    
    recebe um Array2d esq de dimensão (m, n) e outro Array2d dir de dimensão (n, p)
    e retorna o produto matricial entre esq e dir de dimensão (m, p).
    '''
    
    novo = Array2d((esq.shape[0],dir.shape[1]),0)
    posição = 0
    
    for i in range(esq.shape[0]):
        for c in range(dir.shape[1]):
            linha_esq = esq.getlin(i)
            coluna_dir = dir.getcol(c)
            produto = linha_esq.dot(coluna_dir)
            novo.data[posição] = produto
            
            posição += 1
    
    return novo


## ==================================================================

if __name__ == '__main__':
    main()