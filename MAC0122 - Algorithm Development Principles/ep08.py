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

ABRE = '([{'
FECHA = ')]}'

def main():
    ''' função para teste da função bem_formada
    '''

    print('Teste realizado \t\t\t Resultado esperado')
    print('bem_formada("( { } )") = ',{bem_formada("( { } )")},'\t\t\t\t\t True')
    print('bem_formada("{ } ( - ) [ { } (   ) ]") = ',{bem_formada("{ } ( - ) [ { } (   ) ]")},'\t True')
    print('bem_formada("(a + { b } )-{2 *[ 3+4 ]} ") = ',{bem_formada("(a + { b } )-{2 *[ 3+4 ]} ")},' True')
    print('bem_formada("{ ( { x } ) } [ y ]") = ',{bem_formada("{ ( { x } ) } [ y ]")},'\t\t True')
    print('bem_formada("( ( (  )") = ',{bem_formada("( ( (  )")},'\t\t\t\t\t False')
    print('bem_formada(" { ( { x }  } [ y ] )") = ',{bem_formada(" { ( { x }  } [ y ] )")},'\t False')
    print('bem_formada("( { ) }") = ',{bem_formada("( { ) }")},'\t\t\t\t\t False')
    print('bem_formada("{ ( { x } } [ y ] )") = ',{bem_formada("{ ( { x } } [ y ] )")},'\t\t False')
# ---------------------------------------------------------

def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    
    lista = list(seq)
    i = 0
    while i < len(lista):
        if lista[i] not in ABRE and lista[i] not in FECHA:
            del lista[i]
            i -= 1
        i += 1
        
    bem_formada = True
    
    i = 0
    while i < len(lista) and bem_formada:
        if i == 0:
            if lista[0] in FECHA:
                return False

        elif lista[i] not in ABRE:
            if lista[i] == ')':
                if lista[i-1] == '(':
                    lista.pop(i)
                    lista.pop(i-1)
                    i = 0
                else:
                    return False
            elif lista[i] == '}':
                if lista[i-1] == '{':
                    lista.pop(i)
                    lista.pop(i-1)
                    i = 0
                else:
                    return False
            elif lista[i] == ']':
                if lista[i-1] == '[':
                    lista.pop(i)
                    lista.pop(i-1)
                    i = 0
                else:
                    return False
        i += 1

    if len(lista) == 0:
        return True
    else:
        return False
            
# ---------------------------------------------------------

if __name__ == '__main__':
   main()