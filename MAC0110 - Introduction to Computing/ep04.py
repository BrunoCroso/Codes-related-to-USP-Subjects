# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
        
        Este EP foi feito sem ajuda externa.

'''

# escreva seu programa a seguir


num = int(input('Digite n: '))
DV1 = 0
DV2 = 0
ndealgarismos = 0
somaalgarismos = 0
somaalgarismos2 = 0
num4 = num3 = num2 = num

#Cálculo do DV1
while num2 > 0:
    num2 = num2 // 10
    ndealgarismos += 1
x = ndealgarismos
while x > 0:
    somaalgarismos += x*(num3%10)
    num3 = num3 // 10
    x -= 1
if somaalgarismos % 11 == 10:
    DV1 = 0
else:
    DV1 = somaalgarismos % 11

#Cálculo do DV2
y = ndealgarismos - 1
while y > -1:
    somaalgarismos2 += y*(num%10)
    num = num//10
    y -= 1
somaalgarismos2 += ndealgarismos * DV1
if somaalgarismos2 % 11 == 10:
    DV2 = 0
else:
    DV2 = somaalgarismos2 % 11

print(f'DVs = {DV1} {DV2}')
























