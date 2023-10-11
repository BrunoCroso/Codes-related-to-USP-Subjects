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
    foram desenvolvidas e implementadas por mim ou por meu time 
    cujos nomes estão relacionados abaixo e que, portanto, não 
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
    listadas abaixo, e incluo também os nomes de colegas
    do meu time caso essa tenha sido uma atividade em grupo.

    - LISTA de colegas do time 
        - não foi uma atividade em grupo (substitua essa linha caso tenha sido)

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - Somente foi utilizado como fonte externa o livro sugerido na página da disciplina

    - LISTA de outras pessoas que colaboraram na realização do trabalho e
        externas ao grupo.
        - 
'''

# ===================================================================

class Complexo:
    '''Classe utilizada para representar um número Complexo.

    Um complexo é representado por dois números reais. 
    Assim, cada objeto dessa classe terá dois atributos de estado:
 
       * `real`: um número real que corresponde à parte real
       * `imag`: um número real que corresponde à parte imaginária
 
    Você deverá escrever os métodos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, r = 0.0, i = 0.0):
        '''(Complexo, float, float) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os reais `r` e `i` que 
        representam o número complexo.

        Exemplos:

        >>> c0 = Complexo() # construtor chama __init__()
        >>> c0.real
        0.0
        >>> c0.imag
        0.0
        >>> c1 = Complexo(9)
        >>> print(c1.real, c1.imag)
        9.0 0.0
        >>> c2 = Complexo(9,4)
        >>> print(c2.real, c2.imag)
        9.0 4.0
        >>> 
        '''

        self.real = float(r)
        self.imag = float(i)
    
        
    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Complexo) -> str

        Recebe uma referencia `self` a um objeto da classe Complexo e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplos:

        >>> ini = Complexo(8)
        >>> fim = Complexo(9,4)
        >>> fim.__str__()
        '9.0+j4.0'
        >>> ini.__str__() # chamada do método __str__()
        '8.0'
        >>> str(ini) # função str() exibe a string criada por __str__()
        '8.0'
        >>> str(fim) 
        '9.0+j4.0'
        >>> print(fim) # exibe o string criado por __str__()
        9.0+j4.0
        >>> print(ini)
        8.0
        >>>         
        '''

        if self.imag == 0.0:
            return (f'{self.real}')
        elif self.real == 0.0:
            return (f'j{self.imag}')
        else:
            return (f'{self.real}+j{self.imag}')
        
        
    #------------------------------------------------------------------------------        
    def some(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        
        Exemplos:

        >>> c0 = Complexo(8)
        >>> c1 = Complexo(9,4)
        >>> c2 = c0.some(c1)
        >>> print(c2)
        17.0+j4.0
        >>>         
        '''

        pt_real = self.real + other.real
        pt_imag = self.imag + other.imag
        return(Complexo(pt_real,pt_imag))


    #------------------------------------------------------------------------------        
    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado do produto self * other
        
        Exemplos:

        >>> comp0 = Complexo(1, 2)
        >>> comp1 = Complexo(3, 4)
        >>> comp2 = comp0 * comp1
        >>> print(c2)
        -5.0+j10.0
        >>>
        '''

        pt_real = (self.real * other.real) - (self.imag * other.imag)
        pt_imag = (self.real * other.imag) + (self.imag * other.real)
        return(Complexo(pt_real,pt_imag))


