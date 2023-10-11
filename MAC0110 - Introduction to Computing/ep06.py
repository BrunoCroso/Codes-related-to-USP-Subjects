# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
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
        
        Este EP foi feito sem ajuda externa.

"""

#----------------------------------------------------    
def primo(n):
    i = 2
    primo = True
    if n == 1 or n <= 0:
        primo = False
    while i < ((n/2)+1) and primo == True:
        if n % i == 0:
            primo = False
        i += 1
    return primo

#----------------------------------------------------        
def goldbach(n):
    resposta = False,1,1
    q = 1
    while q < n:
        p = 1
        if primo(q) == True:
            while p < n:
                if primo(p) == True:
                    if p + q == n:
                        resposta = True,p,q
                p += 1
        q += 1
    return resposta

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    if d == 0:
        return int(n0)
    else:
        return int((1 + e * p)**d * n0)
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    resposta = n0
    if d > 0:
        i = 1
        infectados_anterior = n0
        infectados = ((1 + e * p * (1 - (infectados_anterior/n)))* (infectados_anterior))
        infectados_anterior = infectados
        resposta = infectados
        while i < d and d != 0:
            infectados = ((1 + e * p * (1 - (infectados_anterior/n)))* (infectados_anterior))
            resposta = infectados
            infectados_anterior = infectados
            i += 1
    return int(resposta)

