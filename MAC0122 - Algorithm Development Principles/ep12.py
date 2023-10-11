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


import numpy as np

## ------------------------------------------------------------------
def main():

    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)  
    print(f"img4:\n{img4}\n")

    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1,2)
    print(f"img6:\n{img6}\n")

## ------------------------------------------------------------------
class NPImagem():
    
    def __init__(self, shape, val = 0):
        ''' (NPImagem, tupla, obj) -> None
        
        Constrói um objeto do tipo NPImagem com os atributos:
        data : array onde os valores são armazenados
        shape: tupla que armazena as dimensões da imagem
        size : número total de elementos da imagem
        '''
        
        if type(val) == np.ndarray:
            self.shape = val.shape
            self.data = val
            self.size = val.size
            
        else:
            self.shape = shape
            self.data = np.full(shape, val)
            self.size = self.shape[0] * self.shape[1]
        

    
    def __str__(self):
        ''' (NPImagem) -> None
        
        Ao ser usada pela função print, exibe o conteudo do atributo data.
        '''
        
        
        return str(self.data)
    
    
    def __getitem__(self, key):
        ''' (NPImagem, tupla) -> obj
        
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do NPImagem self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        '''
        
        dado = self.data[key[0], key[1]]
        return dado
    
    
    def __setitem__(self, key, valor):
        ''' (NPImagem, tupla, obj) -> None
        
        Recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do atributo data de NPImagem.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`.
        '''
        
        self.data[key[0], key[1]] = valor
        return None
    
    
    def crop(self, sup = 0, esq = 0, inf = -1, dir = -1):
        ''' (int, int, int, int) -> NPImagem
        
        Recebe 4 inteiros sup, esq, inf e dir, que definem um retangulo na
        imagem e retorna um NPImagem respectivo a este, sendo:
        sup: primeira linha
        inf: última linha
        esq: primeira coluna
        dir: última coluna
        '''
        
        if inf == -1:
            inf = (self.shape[0])
        
        if dir == -1:
            dir = (self.shape[1])
        
        nova_data = self.data[sup:(inf), esq: (dir)]
        
        retangulo = NPImagem((inf - sup, dir - esq))
        retangulo.data = nova_data
        
        return retangulo
    
    
    
    

## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
