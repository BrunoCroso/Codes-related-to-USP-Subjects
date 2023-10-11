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
# 
def main():
    '''
    Testes da classe Soma 3

    inclua mais 10 testes usando listas diferentes. Por exemplo, 
    o que deve acontecer com listas vazias, listas com números negativos,
    listas ordenadas, etc.
    '''
    print("Testes do EI25 - Soma3")

    testes = [
        [44, 11, 77, 33],
        [],
        [4],
        [4,3],
        [66,99,22],
        [-55,11,99,33],
        [11,22,33,44,55,66,77],
        [-33,66,-99,22],
        [-11,33],
        [-55],
        [-66,-33]
    ]

    for t in testes:
        print(30*'-')
        
        s3 = Soma3(t)
        print(f"\nCriação usando a lista:\nent : {t}")
        print(f"{s3}")

        print("\nDicionário de posições:")
        s3.monte_dicio_pos()
        print(f"{s3}")

        print("\nPares")
        s3.imprima_pares()

        print("\nTrios")
        s3.imprima_trios()

# ===================================================================

class Soma3:

    def __init__(self, seq):
        ''' (Soma3, list) -> None
        '''
        self.data = seq  # faz referência, não copia.
        self.pos = {}

    def __str__(self):
        ''' (Soma3) -> None
        '''
        return f'data: {self.data}\npos : {self.pos}\n'

    # -------------------------------------------------------------------

    def imprima_pares(self):
        ''' (Soma3) -> None

        Imprime todos os pares da lista self.data.
        Exemplo: para self.data = [44, 11, 77, 88]
        o método deve imprimir:
        44  11
        44  77 
        44  88
        11  77
        11  88
        77  88
        '''

        
        for i in range(len(self.data)-1):
            for c in range(i + 1,len(self.data)):
                print(f'{self.data[i]}  {self.data[c]}')

    # -------------------------------------------------------------------

    def imprima_trios(self):
        ''' (Soma3) -> None

        Imprime todos os trios da lista self.data.
        Exemplo: para self.data = [44, 11, 77, 88]
        o método deve imprimir:
        44  11  77
        44  11  88
        44  77  88
        11  77  88
        '''

        for i in range(len(self.data)-2):
            for c in range(i + 1,len(self.data)-1):
                for k in range(c + 1,len(self.data)):
                    print(f'{self.data[i]}  {self.data[c]}  {self.data[k]}')
                
    # -------------------------------------------------------------------

    def monte_dicio_pos(self):
        ''' (Soma3) -> None

        Monta o dicionário self.pos a partir do conteúdo em self.data. 
        Usando cada elemento de self.data como chave, self.pos armazena
        o índice desse elemento na lista self.data. 

        Exemplo: para self.data = [44, 11, 77, 88]
        então self.pos deve conter {44:0, 11:1, 77:2, 88:3}
        '''
        
        for i in range(len(self.data)):
            self.pos[self.data[i]] = i

# ===================================================================

if __name__ == '__main__':
    main()