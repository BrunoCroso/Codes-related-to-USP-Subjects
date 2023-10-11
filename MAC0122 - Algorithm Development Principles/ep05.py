#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS0
#------------------------------------------------------------------

'''

    Nome: Bruno Croso Cunha da Silva
    NUSP: 5524390

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
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
        - Somente foi utilizado como fonte externa o livro sugerido na página da disciplina e a função meu_mdc(), conforme orientado.

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não fui auxiliado por nenhuma pessoa a fazer esse trabalho
'''

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction.
    '''

    # Criação de objetos do tipo Fraction 
    f12 = Fraction(1,2)
    f34 = Fraction(3,4)

    # soma 2 fracoes
    soma = f12 + f34
    print(f"{f12} + {f34}      = {soma}")
    print(f"Resultado esperado = 5/4 ")


    # soma fracao com inteiro
    soma = f12 + 2
    print(f"{f12} + 2         = {soma}")
    print(f"Resultado esperado = 5/2 ")

    # soma inteiro com fracao
    soma = 2 + f34
    print(f"2 + {f34}      = {soma}")
    print(f"Resultado esperado = 11/4 ")
    


    # ===================================================================
    # Escreva outros testes

    #Testes divisão
    divisao = f12 / 2
    print(f"{f12} / 2         = {divisao}")
    print(f"Resultado esperado = 1/4 ")
    
    divisao = f12 / f34
    print(f"{f12} / {f34}         = {divisao}")
    print(f"Resultado esperado = 2/3 ")
       
    divisao = 2 / f34
    print(f"2 / {f34}         = {divisao}")
    print(f"Resultado esperado = 8/3 ")
    
    
    #Testes igualdade
    
    igualdade = f12 == f34
    print(f"{f12} == {f34}         = {igualdade}")
    print(f"Resultado esperado = False ")
    
    igualdade = f12 == Fraction(4,8)
    print(f"{f12} == {Fraction(4,8)}         = {igualdade}")
    print(f"Resultado esperado = True ")
    
    igualdade = Fraction(12,4) == 2
    print(f"{Fraction(12,4)} == 2         = {igualdade}")
    print(f"Resultado esperado = False ")
    
    igualdade = Fraction(12,4) == 3
    print(f"{Fraction(12,4)} == 3        = {igualdade}")
    print(f"Resultado esperado = True ")

    igualdade = 2 == Fraction(12,4)
    print(f"2 == {Fraction(12,4)}         = {igualdade}")
    print(f"Resultado esperado = False ")
    
    igualdade = 3 == Fraction(12,4)
    print(f"3 == {Fraction(12,4)}        = {igualdade}")
    print(f"Resultado esperado = True ")


    #Testes de >
    
    maior = f12 > f34
    print(f"{f12} > {f34}         = {maior}")
    print(f"Resultado esperado = False ")
    
    maior = f34 > f12
    print(f"{f34} > {f12}         = {maior}")
    print(f"Resultado esperado = True ")
    
    maior = f34 > Fraction(12,16)
    print(f"{f34} > {Fraction(12,16)}         = {maior}")
    print(f"Resultado esperado = False ")

    maior = Fraction(9,4) > 2
    print(f"{Fraction(9,4)} > {2}         = {maior}")
    print(f"Resultado esperado = True ")

    maior = Fraction(9,4) > 3
    print(f"{Fraction(9,4)} > {3}         = {maior}")
    print(f"Resultado esperado = False ")

    maior = 3 > f34
    print(f"{3} > {f34}         = {maior}")
    print(f"Resultado esperado = True ")

    maior = 2 > Fraction(15,4)
    print(f"{f12} > {f34}         = {maior}")
    print(f"Resultado esperado = False ")    
    
    
    
    
    #Testes de <=
    
    menor_igual = f12 <= f34
    print(f"{f12} <= {f34}         = {menor_igual}")
    print(f"Resultado esperado = True ")
    
    menor_igual = f34 <= f12
    print(f"{f34} <= {f12}         = {menor_igual}")
    print(f"Resultado esperado = False ")
    
    menor_igual = Fraction(9,4) <= 3
    print(f"{Fraction(9,4)} <= {3}         = {menor_igual}")
    print(f"Resultado esperado = True ")
    
    menor_igual = 3 <= f34
    print(f"{3} <= {f34}         = {menor_igual}")
    print(f"Resultado esperado = False ")
    
    menor_igual = 5 <= Fraction(15,3)
    print(f"{5} <= {Fraction(15,3)}         = {menor_igual}")
    print(f"Resultado esperado = True ")
    



# ===================================================================
#
#   No futuro substituiremos a definição da classe por um import. 
#
# ===================================================================


class Fraction:
    '''
        Essa classe Fraction foi adaptada da seção 1.13.1 Uma Classe Fraction
        do capítulo 1 do livro Resolução de Problemas com Algoritmos e 
        Estruturas de Dados usando Python disponível no endereço
        https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. 

        A classe Fraction representa uma fração. 
        Uma fração é constituída por um numerador e um denominador, 
        ambos inteiros, como por exemplo 2/5 (dois quintos), 
        onde 2 é o numerador e 5 o denominador.
    '''

    def __init__(self, cima, baixo):
        '''(Fraction, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros cima e baixo que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        '''
        self.num = cima
        self.den = baixo

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> frac = Fraction(2,5)
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"

    #------------------------------------
    
    def meu_mdc( self, a, b ):
        ''' (Fraction, int, int) -> int 
        recebe dois inteiros a e b, e 
        retorna o mdc entre a e b.
        '''
        aa = abs(a)
        ab = abs(b)
        mdc = min(aa, ab)
        if mdc == 0: return max(aa, ab)
        while (aa % mdc != 0) or (ab % mdc != 0): 
            mdc -= 1
        return mdc
    
    def __add__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a soma da Fraction `self` e da Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction + Fraction ou
                                            Fraction + int
        """
        
        if type(other) is int:
            numerador = self.num + (self.den * other) 
            denominador = self.den
            
        else:
            num_intermediario = self.num * other.den + self.den * other.num
            den_intermediario = self.den * other.den
            menor_divisor_comum = self.meu_mdc(num_intermediario,den_intermediario)
            numerador = num_intermediario // menor_divisor_comum
            denominador = den_intermediario // menor_divisor_comum
            
        return Fraction(numerador,denominador)
    
    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        return self + other

    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """
        
        if type(other) is int:
            num_intermediario = self.num
            den_intermediario = self.den * other
            menor_divisor_comum = self.meu_mdc(num_intermediario,den_intermediario)
            numerador = num_intermediario // menor_divisor_comum
            denominador = den_intermediario // menor_divisor_comum
            
        else:
            num_intermediario = self.num * other.den
            den_intermediario = self.den * other.num
            menor_divisor_comum = self.meu_mdc(num_intermediario,den_intermediario)
            numerador = num_intermediario // menor_divisor_comum
            denominador = den_intermediario // menor_divisor_comum
            
        return Fraction(numerador,denominador)

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        
        num_intermediario = self.den * other
        den_intermediario = self.num
        menor_divisor_comum = self.meu_mdc(num_intermediario,den_intermediario)
        numerador = num_intermediario // menor_divisor_comum
        denominador = den_intermediario // menor_divisor_comum
        
        return Fraction(numerador,denominador)

    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        
        
        if type(other) is int:
            if (self.num/self.den) == other:
                return True
            else:
                return False

        else:
            mdc_self = self.meu_mdc(self.num,self.den)
            mdc_other = self.meu_mdc(other.num,other.den)
            if (self.num / mdc_self) == (other.num / mdc_other):
                if (self.den / mdc_self) == (other.den / mdc_other):
                    return True
                else:
                    return False
            else:
                return False
        

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """

        return self == other
    
    #-------------------------------------
    
    def __gt__(self, other):
        """ (Fraction, Fraction ou int) -> bool
        
        Retorna se o int 'other' é maior (ou não) que a Fraction 'self'.
        Usado pelo Python quando escrevemos Fraction > Fraction ou
                                            Fraction > int
        """
    
        if type(other) is int:
            if self.num > (self.den * other):
                return True
            else:
                return False
            
        else:
            if (self.num * other.den) > (self.den * other.num):
                return True
            else:
                return False
        

    #-------------------------------------
    
    def __rgt__(self, other):
        """ (Fraction, int) -> bool
        
        Retorna se a Fraction `self` é maior (ou não) que a Fraction ou int `other`.
        Usado pelo Python quando escrevemos int > Fraction
        O método __rgt__ não é um método padrão do Python, sendo o método chamado ao escrevermos int > Fraction o __lt__ (o qual faz Fraction < int, uma exprressão equivalente).
        Abaixo, encrontra-se o método __rgt__ caso fosse chamado e o método __lt__, o qual serve como "equivalente" à __rgt__ neste código.

        """    
             
        if (other * self.den) > self.num:
            return True
        
        else:
            return False

    
    def __lt__(self, other):
        """ (Fraction, Fraction ou int) -> bool
        
        Retorna se o int 'other' é menor (ou não) que a Fraction 'self'.
        Usado pelo Python quando escrevemos Fraction < Fraction ou
                                            Fraction < int
                                            
        Utilizado como "equivalente" a __rgt__, sendo chamada quando escrevemos int > Fraction.
        """    
    
        if type(other) is int:
            if self.num < (self.den * other):
                return True
            else:
                return False
            
        else:
            if (self.num * other.den) < (self.den * other.num):
                return True
            else:
                return False
    
    
    
    
    #-------------------------------------
    
    def __le__(self, other):
        """ (Fraction, Fraction ou int) -> bool
        
        Retorna se a Fraction `self` é menor ou igual que a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction <= Fraction ou
                                            Fraction <= int
                                            
        """
        
        if type(other) is int:
            if self.num <= (self.den * other):
                return True
            else:
                return False
            
        else:
            if (self.num * other.den) <= (self.den * other.num):
                return True
            else:
                return False
        
        
        
    #-------------------------------------

            
    def __rle__(self, other):
        """ (Fraction, int) -> bool
        
        Retorna se o int 'other' é menor ou igual que a Fraction 'self'.
        Deveria ser usado pelo Python quando escrevemos int <= Fraction
        O método __rle__ não é um método padrão do Python, sendo o método chamado ao escrevermos int <= Fraction o __ge__ (o qual faz Fraction >= int, uma expressão equivalente).
        Abaixo, encrontra-se o método __rle__ caso fosse chamado e o método __ge__, o qual serve como "equivalente" à __rle__ neste código.
        """
    
        if (other * self.den) <= self.num:
            return True
        
        else:
            return False
    
    
    
    def __ge__(self, other):
        """ (Fraction, Fraction ou int) -> bool
        
        Retorna se o int 'other' é menor (ou não) que a Fraction 'self'.
        Usado pelo Python quando escrevemos Fraction >= Fraction ou
                                            Fraction >= int
                                            
        Utilizado como "equivalente" a __rle__, sendo chamada quando escrevemos int <= Fraction.
        """  
        if type(other) is int:
            if self.num >= (self.den * other):
                return True
            else:
                return False
            
        else:
            if (self.num * other.den) >= (self.den * other.num):
                return True
            else:
                return False
        
        

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()