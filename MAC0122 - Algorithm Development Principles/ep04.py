#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
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
        - Somente foi utilizado como fonte externa o livro sugerido na página da disciplina
        - Deste livro, foi retirada a função , a qual foi utilizada somente para que os resultados estivessem em sua forma irredutivel.

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


# ===================================================================
#
#   No futuro substituiremos a definição da classe por um import. 
#
# ===================================================================

def mdc(m, n):
    '''
    (int,int) -> (int)
    Recebe 2 inteiros e retorna o menor divisor comum entre eles
    Esta função foi retirada do livro "Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python".
    '''
    while m%n != 0:
        mvelho = m
        nvelho = n

        m = nvelho
        n = mvelho%nvelho
    return n

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
            menor_divisor_comum = mdc(num_intermediario,den_intermediario)
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
            menor_divisor_comum = mdc(num_intermediario,den_intermediario)
            numerador = num_intermediario // menor_divisor_comum
            denominador = den_intermediario // menor_divisor_comum
            
        else:
            num_intermediario = self.num * other.den
            den_intermediario = self.den * other.num
            menor_divisor_comum = mdc(num_intermediario,den_intermediario)
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
        menor_divisor_comum = mdc(num_intermediario,den_intermediario)
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
            mdc_self = mdc(self.num,self.den)
            mdc_other = mdc(other.num,other.den)
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

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()