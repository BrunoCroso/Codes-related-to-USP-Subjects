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

#------------------------------------------------------
def main():
    '''
    Testes para os algoritmos de LCS

    Inclua ao menos 10 testes distintos para sua função subseq().
    '''
    print("Testes para sua função subseq()")
    print("--------------------------------\n")

    print("Exemplos de execuções de lcs_rec()")
    print("----------------------------------")
    print("teste 0:")
    s = 'abracadabra'
    t = 'yabbadabbadoo'
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")
    
    print("teste 1:")
    s = 'tagctgaatc'
    t = 'tatactgcctt'
    LCS = lcs_rec(s,t)
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")
    
    print("teste 2:")
    s = 'caattttataccgcagc'
    t = 'gaataggtatcgcca'
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")

    '''
    print("teste 3:")
    s = 'taggcagggcacgccaccttatg'
    t = 'tccgtttctaaaccatacaaacctcct'
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")
    
    print("teste 4:")
    s = 'gaaccgcaggaattttcgcttgatccaacgaacca'
    t = 'ggtatacggggctttctagaccaaggaaaat'
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")
    
    print("teste 5:")
    s = 'tctgggaatgcggtctcgcttagctgcggggacgacgagcagtgaacgacgcttcccacgc'
    t = 'ttatggctcactaccacggccaaagaggtagagcacattttctacccaggctgaggtgtcctcttaccttt'
    print(f"s={s}\nt={t}\nLCS(s,t)={lcs_rec(s,t)}\n-----")
    '''
    
    print('\nTestes para subseq (s, t)\n')
    
    pares = [['abcde','abc'],
             ['abcde','acd'],
             ['abcde','ae'],
             ['aaaaa','aa'],
             ['aaaaa', 'ad'],
             ['aaaaa','da'],
             ['tatactgcctt',LCS],
             ['',''],
             ['','a'],
             ['a','']]
    
    for i in range(len(pares)):
        print(f't = {pares[i][0]}')
        print(f's = {pares[i][1]}')
        teste = subseq(pares[i][1], pares[i][0])
        if teste == True:
            print('s É subsequencia de t\n')
        else:
            print('s NÃO É subsequencia de t\n')
        
       
    #----------------------------------------------
def subseq (s, t):
    ''' (str, str) -> bool 
    RECEBE strings s e t.
    RETORNA True se s é subsequência de t.
    '''
    
    
    if len(s) == 0:
        return True
    
    if len(s) > len(t):
        return False
    
    cont_s = 0
    cont_t = 0
    
    while cont_t <= (len(t)+1):
        if s[cont_s] == t[cont_t]:
            cont_s += 1
            cont_t += 1
            
        else:
            cont_t += 1
            
        if cont_s == len(s):
            return True
            
        if cont_t == len(t):
            return False
    
    return False
#----------------------------------------------
def lcs_rec(s, t):
    '''(str, str) -> str
    INTERFACE para a função recursiva lcs_rec.
    '''
    m = len(s)
    n = len(t)
    return lcsR(s, m, t, n)

#----------------------------------------------
def lcsR(s, m, t, n):
    '''(str, int, str, int) -> str
    RECEBE uma string s, um inteiro m, uma string t e um inteiro n.
    RETORNA uma LCS de s[0:m] e t[0:n].
    '''
    # BASE
    if m == 0 or n == 0: return ""

    # REDUZ 
    if s[m-1] == t[n-1]:
        return lcsR(s, m-1, t, n-1) + s[m-1]
    
    # REDUZ
    lcs_1 = lcsR(s, m-1, t,   n)
    lcs_2 = lcsR(s,   m, t, n-1)

    # COMBINA
    if len(lcs_1) > len(lcs_2): return lcs_1
    return lcs_2

#----------------------------------------------------
if __name__ == "__main__":
    main()
    
