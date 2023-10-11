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
        - Somente foi utilizado como ferramenta auxiliar a correção da Atividade
        de Revisão anterior

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não recebi ajuda externa 
'''

## ==================================================================


import numpy as np

## ------------------------------------------------------------------
def main():

    print("======Teste operadores\n")

    imgA = NPImagem( (2,3), 5)
    imgB = NPImagem( (), np.arange(20).reshape(5,4) )
    imgC = imgB.crop(2,1,4,4)
    imgD = imgA + imgC
    print(f"imgA:\n{imgA}")
    print(f"imgB:\n{imgB}")
    print(f"imgC:\n{imgC}")
    print(f"imgD:\n{imgD}")

    print("\n===== Crop ========\n")

    lista = list(range(30))
    ar = np.array(lista).reshape(6,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 88)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[2,1]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    print("======Teste pinte_retangulo\n")
    img1.pinte_retangulo(1,2,3,5,77)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")

    img2.pinte_retangulo(-1,-2,2,3,99)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")

    img3.pinte_retangulo(1,0,3,4,66)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")

    print("======Teste paste\n")
    img1 = NPImagem( (0, 0), ar)  # 
    img2 = NPImagem( (2, 3), 99)
    img3 = img1.crop(2,1,5,3) ## cria uma cópia
    print(f"img1:\n{img1}")
    print(f"img2:\n{img2}")
    print(f"img3:\n{img3}")

    img1.paste(img2, 2, 3)
    print(f"img1.paste(img2,2,3):\n{img1}\n")

    img1.paste(img3, 4, 2 )
    print(f"img1.paste(img3,4,2):\n{img1}\n")

    img1.paste(img3, -1, 2)
    print(f"img1.paste(img3,-1,2):\n{img1}\n")

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
            self.shape = val.copy().shape
            self.data = val.copy()
            self.size = val.copy().size
            
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
        
        nova_data = self.data.copy()[sup:(inf), esq: (dir)]
        
        retangulo = NPImagem((inf - sup, dir - esq))
        retangulo.data = nova_data
        
        return retangulo
    
    def pinte_retangulo(self, sup, esq, inf, dir, v=0):
        ''' (NPImagem, int, int, int, int, int) -> None 
        
        Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
        o canto inferior-direito (inf,dir) de uma região retangular com 
        relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos" 
        em pixeis com relação à origem.
        Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição com o retângulo (sup,esq)x(inf,dir). 
        '''
        
        
        
        linhas_ret = inf - sup
        colunas_ret = dir - esq
        
        if sup >= self.shape[0]:
            return None
        if esq >= self.shape[1]:
            return None
        if inf <= 0  or dir <= 0:
            return None
        
        sup_real = max(0, sup)
        inf_real = min(sup + linhas_ret, self.shape[0])
        esq_real = max(0, esq)
        dir_real = min(esq + colunas_ret, self.shape[1])
        
        self.data[sup_real:inf_real, esq_real:dir_real] = v


    
    def paste(self, other, sup, esq):
        '''(NPImagem, NPImagem, int, int) -> None
        
        Recebe um objeto NPImagem other e um par de inteiros (sup, esq) 
        que indica um deslocamento em relação à origem de self (posição (0,0)) 
        onde a NPImagem other deve ser sobreposta sobre self. Observe que
        esse deslocamento pode ser negativo. Nesse caso, a dimensão de other
        define o canto inferior-direito do retângulo.
        ''' 
         
        
        maximo_inf = sup + other.shape[0]
        maximo_dir = esq + other.shape[1]
     
        if sup >= self.shape[0]:
            return None
        if esq >= self.shape[1]:
            return None
        if maximo_inf <= 0  or maximo_dir <= 0:
            return None
     
        self_sup = max(0, sup)
        self_esq = max(0, esq)
        self_inf = min(maximo_inf, self.shape[0])
        self_dir = min(maximo_dir, self.shape[1])
        
        other_sup = -min(0, sup)
        other_esq = -min(0, esq)
        other_inf = other_sup + self_inf - self_sup
        other_dir = other_esq + self_dir - self_esq
     
        self.data[self_sup:self_inf, self_esq:self_dir] = other.data[other_sup:other_inf, other_esq:other_dir]
     

     
        
    def __add__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna a soma, elemento-a-elemento,
        dos pixels de self e other.
        '''
        
        nlins = self.shape[0]
        ncols = self.shape[1]
        
        soma = NPImagem((nlins,ncols),0)
        
        for c in range(nlins):
            for i in range(ncols):
                soma.data[c][i] = self.data[c][i] + other.data[c][i]
        
        return soma
    
    
    def __mul__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna o produto, elemento-a-elemento,
        dos pixels de self e other.
        '''

        nlins = self.shape[0]
        ncols = self.shape[1]
        
        mult = NPImagem((nlins,ncols),0)
        
        for c in range(nlins):
            for i in range(ncols):
                mult.data[c][i] = self.data[c][i] * other.data[c][i]
        
        return mult

## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
