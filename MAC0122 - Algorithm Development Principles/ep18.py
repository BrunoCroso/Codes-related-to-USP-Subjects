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


def main():
    x = [    
            8, 8, 8, 8, 1, 4,
            1, 8, 1, 1, 1, 4,
            1, 8, 8, 1, 4, 4,
            1, 1, 1, 1, 4, 4,
            1, 9, 1, 4, 1, 4,
            9, 9, 9, 9, 1, 4
        ]

    img = np.array(x).reshape(6,6)
    print(f'Imagem\n', img)

    # cria um objeto Blobs usando img
    blobs = Blobs(img)

    # vamos ver as blobs
    dt = blobs.data
    n = len(dt)
    
    for i in range(n):
        elem = list(dt[i])[0] # pega um elemento do conjunto
        print(f'blob {i} tem tamanho {len(dt[i])} e cor {img[elem]}')
        print(f'   {dt[i]}')    


## ==================================================================

class Blobs:

    def __init__(self, img):
        ''' (Blobs, array) -> None 
        construtor da classe Blobs.
        '''

        self.data = []
        self.img = img
        self.segmente(img) # deve carregar self.data
        ## inclua outros atributos que desejar

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Blobs) -> str
        retorna uma string com a descrição das blobs.
        '''
        
        txt = ''
        dt = self.data
        n = len(dt)
        for i in range(n):
            txt += f'blob {i} tem tamanho {len(dt[i])}\n'
            txt += f'   {dt[i]}\n'
        return txt

    # ---------------------------------------------------------------
    def segmente(self, img):
        ''' (Blobs, array) -> None
        Método usado pelo construtor para segmentar todas
        as blobs da imagem img.
        '''

        
        blobs = []
        repetidos = []
        for i in range(len(img)):
            for c in range(len(img[0])):
                posicao = (i,c)
                if posicao not in repetidos:
                    blob = self.segmente_blob( img, posicao )
                    sete = set()
                    for cont in blob:
                        sete.add(cont)
                        repetidos.append(cont)
                    blobs.append(sete)
                    
                    
        self.data = blobs



    # ---------------------------------------------------------------
    def segmente_blob( self, img, semente ):
        ''' (Blobs, ndarray, tuple) -> set

            interface para o método self.segmente_blob_RM.
            Cria um conjunto vazio que é carregado
            de forma recursiva.  
            
            Não altere esse método.
        '''
        return self.segmente_blob_RM( img, semente, set() )

    # ---------------------------------------------------------------
    def segmente_blob_RM(self, img, semente, visitados ):
        ''' (Blobs, ndarray, tuple, set) -> set

        Recebe, além de self, um ndarray img e uma tupla semente contendo a
        coordenada de um pixel de img. Recebe também o conjunto
        visitados, que contém as coordenadas dos pixels já 
        visitados.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        final = set()
        final.add(semente)
        padrao = img[semente[0]][semente[1]]
        
        proximos = set()
        proximos.add((semente[0]-1,semente[1]))
        proximos.add((semente[0]+1,semente[1]))
        proximos.add((semente[0],semente[1]-1))
        proximos.add((semente[0],semente[1]+1))
        
        if semente[0] == 0:
            proximos.remove((semente[0]-1,semente[1]))
            
        elif semente[0] == len(img)-1:
            proximos.remove((semente[0]+1,semente[1]))
        
        if semente[1] == 0:
            proximos.remove((semente[0],semente[1]-1))
        
        elif semente[1] == len(img[0])-1:
            proximos.remove((semente[0],semente[1]+1))
        
        copia = []
        for i in proximos:
            copia += [i]
        
        for i in copia:
            if i in visitados:
                proximos.remove(i)
        
        for i in proximos:
            visitados.add(i)
            if img[i[0]][i[1]] == padrao:
                final.add(i)
                for i in self.segmente_blob_RM( img, i, visitados ):
                    final.add(i)
    
        return final
    

    ## ==================================================================

    def pinte_blob( self, img, blob, nova_cor = 0):
        ''' (Blobs, ndarray, set, int) -> None

        Recebe, além de self, um ndarray img e um conjunto de pixels blob
        e pinta esses pixels com a nova_cor.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        for i in blob:
            img[i[0]][i[1]] = nova_cor
            
            
## ==================================================================
## Coloque aqui outras funções e métodos que desejar

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    