# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome: Bruno Croso Cunha da Silva
    NUSP: 5524390

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#------------------------------------------------------------------
# Constantes que você pode utilizar nesse exercício
# Em notação científica 1.0e-6 é o o mesmo qoe 0.000001 (10 elevado a -6)
EPSILON  = 1.0e-6

#------------------------------------------------------------------
# O import abaixo permite que o programa utilize todas as funções do módulo math,
# como por exemplo, math.exp e  math.sin.
import math

#------------------------------------------------------------------
def main():
    '''() -> None

    Modifique essa função, escrevendo outros testes.
    '''
    # escolha a função que desejar e atribuia a f_x
    # f_x = math.cos 
    # f_x = math.sin 
    # f_x = math.exp # etc, para integração com outras funções.
    # f_x = identidade     # identidade() definidas mais adiante
    # f_x = circunferencia # circunferencia() definida mais adiante
    # f_x = exp            # exp() definida mais adiante
 
    print("Início dos testes.")
    # Testes da f_x
    f_x = math.cos
    nome = f_x.__name__ # nome da f_x usada
    print(f"A função f_x usada nos testes é {nome}()")
    print(f"Valor de f_x(0.0)= {f_x( 0.0 )}")
    print(f"Valor de f_x(0.5)= {f_x( 0.5 )}")
    print(f"Valor de f_x(1.0)= {f_x( 1.0 )}")

    # testes da função área_por_retangulos
    print()
    print("Área por retângulos:")
    a, b = 0, 1 # intervalo [a,b]
    k = 1       # número de retângulos
    n = 3       # número de iterações
    i = 0
    while i < n:    
        print(f"teste {i+1}: para {k} retângulos no intervalo [{a}, {b}]:")
        print(f"    área aproximada = {area_por_retangulos(f_x, a, b, k):g}")
        k *= 10 
        i += 1

    # testes da função área_aproximada
    print()
    print("Área aproximada:")
    a, b = 0, 1 # intervalo
    k, area = area_aproximada(f_x, a, b) # número de retângulos e aproximação
    print(f"teste 1: para eps = {EPSILON:g} e intervalo [{a}, {b}]:")
    print(f"     com {k} retângulo a área é aproximadamente = {area:g}")
    eps = 1e-6 # erro relativo aceitável
    i = 1 
    n = 4
    while i < n: 
        eps *= 10 # aumenta o erro relativo aceitável
        k, area = area_aproximada(f_x, a, b, eps)
        print(f"teste {i+1}: para eps = {eps:g} e intervalo [{a}, {b}]:")
        print(f"     com {k} retângulos a área é aproximadamente = {area:g}")
        i += 1
 
    print("Fim dos testes.")
    
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x)=x
def identidade( x ):
    return x

#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x)=sqrt(1 - x*x)
def circunferencia( x ):
    y = math.sqrt( 1 - x*x )    
    return y
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função f(x) = e^x
def exp( x ):
    y = math.exp( x )
    return y # return math.exp( x ) 

#------------------------------------------------------------------
#
def erro_rel(y, x):
    if x == 0 and y == 0:
        return 0.0
    elif x == 0:
        return 1.0
    erro = (y-x)/x
    if erro < 0:
        return -erro
    return erro

#------------------------------------------------------------------
def area_por_retangulos(f, a, b, k):
    '''(function, float, float, int) -> float

    RECEBE uma função f, dois números a e b e um inteiro k.
    RETORNA uma aproximação da área sob a função f no intervalo [a,b] 
        usando k retângulos.
    PRÉ-CONDIÇÃO: a função supõe que a função f é continua no intervalo [a,b] e que 
         f(x) >= 0 para todo x, a <= x <= b.
    EXEMPLOS:
    In [15]area_por_retangulos(identidade, 0, 1, 1)
    Out[15]: 0.5
    In [16]:area_por_retangulos(circunferencia, -1, 0, 1)
    Out[16]: 0.8660254037844386            
    '''
    base = (b - a)/k
    i = 0
    area = 0.0
    while i < k:
       ponto_medio = (a + base/2) + i * base 
       altura = f(ponto_medio)
       area += (altura * base)
       i += 1
    return area

#------------------------------------------------------------------
def area_aproximada(f, a, b, eps=EPSILON):
    '''(function, float, float, float) -> int, float

    RECEBE uma função f, dois números a, b, eps.
    RETORNA um inteiro k e uma aproximação da área sob a função f no intervalo [a,b] 
        usando k retângulo.

    O valor de k deve ser a __menor potência__ de 2 tal que o erro relativo 
    da aproximação retornada seja menor que eps.

    Assim, os possíveis valores de k são 1, 2, 4, 8, 16, 32, 64, ...

    PRÉ-CONDIÇÃO: a função supõe que a função f é continua no intervalo [a,b] e que 
         f(x) >= 0 para todo x, a <= x <= b.
         
    EXEMPLOS:
    In [22]: area_aproximada(identidade, 1, 2)
    Out[22]: (2, 1.5)

    In [23]: area_aproximada(exp, 1, 2, 16)
    Out[23]: (2, 4.6224728167337865)  
    '''
    parada = False
    i = 1
    k_ideal = 1
    area = 0.0
    while parada == False:
        k = 2 ** i
        if erro_rel(area_por_retangulos(f, a, b, k/2), area_por_retangulos(f, a, b, k)) < eps:
             k_ideal = k
             area = area_por_retangulos(f, a, b, k)
             parada = True
        i += 1
    return  k_ideal, area  

#######################################################
###                 FIM                             ###
#######################################################
# 
#  NÃO MODIFIQUE AS LINHAS ABAIXO
# 
# Esse if serve para executar a função main() apenas quando
# este é o módulo a partir do qual a execução foi iniciada.
if __name__ == '__main__':
    main()
