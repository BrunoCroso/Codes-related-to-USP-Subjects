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
        Este EP foi feito sem ajuda externa.

'''
# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    print("início dos testes")
    print('')
    
    #Testes gera_gap
    
    print('\tTestes GERA_GAP:')
    
    if gera_gaps( 'T' ) == ['_T', 'T_']:
        print ('\tPassou no teste 1')
    else:
        print ('\tNÃO PASSOU no teste 1')
        
    if gera_gaps( 'CA' ) == ['_CA', 'C_A', 'CA_']:
        print ('\tPassou no teste 2')
    else:
        print ('\tNÃO PASSOU no teste 2')
        
    if gera_gaps( 'AT_G') == ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_']:
        print ('\tPassou no teste 3')
    else:
        print ('\tNÃO PASSOU no teste 3')
        
            
    #testes pontuacao
    
    print('')
    print('\tTestes PONTUACAO:')
    
    if pontuacao('T_', 'CT', 1, 5, 6, 3) == -9:
        print ('\tPassou no teste 1')
    else:
        print ('\tNÃO PASSOU no teste 1')
        
    if pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3) == 12:
        print ('\tPassou no teste 2')
    else:
        print ('\tNÃO PASSOU no teste 2')
        
    if pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4) == -10:
        print ('\tPassou no teste 3')
    else:
        print ('\tNÃO PASSOU no teste 3')
        
    if pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2) == 9:
        print ('\tPassou no teste 4')
    else:
        print ('\tNÃO PASSOU no teste 4')
            
            
    ## Escreva aqui os testes para a função gera_gaps
    # 

    ## Escreva aqui os testes para a função pontuação
    #  Comece por exemplo escrevendo os exemplos mostrados 
    #  nesse arquivo, na especificação de cada função.    
    print('')
    print("fim dos testes")


#------------------------------------------------------------------
#
def gera_gaps(dna):
    ''' ( str ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (GAP).

    RETORNA uma lista com todas as variações de dna com um símbolo GAP 
    a mais e sem repetições.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    variações = []    
    for i in range (len(dna) + 1):
        primeira_metade = dna[:i]
        segunda_metade = dna[i:]
        novo = primeira_metade + '_' + segunda_metade
        if variações.count(novo) == 0:
            variações.append(novo)
    return variações

#------------------------------------------------------------------
#
def pontuacao(s, t, ga, la, ldif, lgap):
    ''' (str, str, int, int, int, int) -> int

    RECEBE duas strings `s` e `t` de mesmo tamanho com zero ou mais gaps 
    representando fitas de DNA; e quatro inteiros `ga`, `la`, `ldif`, `lgap`.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:

       * dois gaps alinhados contam `ga` pontos,
       * duas letras iguais alinhadas contam `la` pontos, 
       * duas letras diferentes alinhadas contam `-ldif` pontos (subtrai ldif pontos) e 
       * uma letra alinhada com um gap contam `-lgap` pontos (subtrai lgap pontos).

    Exemplos:

    In  [1]: pontuacao('T_', 'CT', 1, 5, 6, 3)
    Out [1]: -9

    In  [2]: pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)
    Out [2]: 12
    
    In  [3]: pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)
    Out [3]: -10
    
    In  [4]: pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2)
    Out [4]: 9
    '''
    # modifique o código abaixo para conter a sua solução.
    
    contador_dois_gaps_alinhados = 0
    contador_duas_letras_iguais_alinhadas = 0
    contador_duas_letras_diferentes_alinhadas = 0
    contador_letra_e_gap_alinhados = 0
    
    for i in range (len(s)):
        
        if (s[i] == '_') and (t[i] == '_'):
            contador_dois_gaps_alinhados += 1
            
        if (s[i] == t[i]) and (s[i] != '_'):
            contador_duas_letras_iguais_alinhadas += 1
        
        if (s[i] != '_') and (t[i] != '_') and (s[i] != t[i]):
            contador_duas_letras_diferentes_alinhadas += 1
        
        if ((s[i] == '_') and (t[i] != '_')) or ((s[i] != '_') and (t[i] == '_')):
            contador_letra_e_gap_alinhados += 1      
            
    pontuação = (contador_dois_gaps_alinhados * ga) + (contador_duas_letras_iguais_alinhadas * la) - (contador_duas_letras_diferentes_alinhadas * ldif) - (contador_letra_e_gap_alinhados * lgap)
    
    return pontuação
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
