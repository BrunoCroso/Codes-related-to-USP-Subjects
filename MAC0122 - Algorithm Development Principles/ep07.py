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
## Escreva a sua função palindromo()

def palindromo(s = 0):
    ''' (str or int) -> (bool)
    
    Recebe uma string s e retorna True se for um palindromo e False caso contrário
    '''
    
    A = ['á','à','â','ã']
    E = ['é','è','ê']
    I = ['ú','ù','û']
    O = ['ó','ò','ô','õ']
    U = ['ú','ù','û']
    sinais = [' ','-','_','!','.','?',';',':',',']
    

    if type(s) == str:
        s = s.lower()
        pilha = Pilha()
        for i in range (len(s)):
            pilha.empilhe(s[i])
    
        lista = pilha.dados[:]
    
        pilha_inversa = Pilha()
        for i in range (len(s)):
            último_item = pilha.desempilhe()
            pilha_inversa.empilhe(último_item)
    
        lista_inversa = pilha_inversa.dados[:]
        
        
        for c in range (len(lista)):
            if lista[c] in A:
                lista[c] = 'a'
            if lista_inversa[c] in A:
                lista_inversa[c] = 'a'
            if lista[c] in E:
                lista[c] = 'e'
            if lista_inversa[c] in E:
                lista_inversa[c] = 'e'
            if lista[c] in I:
                lista[c] = 'i'
            if lista_inversa[c] in I:
                lista_inversa[c] = 'i'
            if lista[c] in O:
                lista[c] = 'o'
            if lista_inversa[c] in O:
                lista_inversa[c] = 'o'
            if lista[c] in U:
                lista[c] = 'u'
            if lista_inversa[c] in U:
                lista_inversa[c] = 'u'
            
                
        cont_lista = 0
        while cont_lista < (len(lista)):
            if lista[cont_lista] in sinais:
                del(lista[cont_lista])
                cont_lista -= 1
            cont_lista += 1
            
        cont_lista_inversa = 0
        while cont_lista_inversa < (len(lista_inversa)):
            if lista_inversa[cont_lista_inversa] in sinais:
                del(lista_inversa[cont_lista_inversa])
                cont_lista_inversa -= 1
            cont_lista_inversa += 1   


        return lista == lista_inversa
    
    else:
        num = s
        oposto = []
        while num != 0:
            ultimo_digito = num % 10
            oposto.append(ultimo_digito)
            num = num // 10
            
        normal = []
        for i in range (len(oposto)-1,-1,-1):
            normal.append(oposto[i])
            
        return normal == oposto
            
            
            

## ==================================================================
##
class Pilha:

    def __init__(self):
        '''(Pilha) -> (None)
        
        Chamada pelo construtor para criar uma pilha vazia
        '''
        
        self.dados = []
        
    def __str__(self):
        '''(Pilha) -> (str)

        Recebe uma referencia `self` a um objeto da classe Pilha e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  
        '''        
        
        return str(self.dados)
    
    def vazia(self):
        '''(Pilha) -> (bool)

        Recebe uma referencia `self` a um objeto da classe Pilha e
        cria e retorna True se essa está vazia e False caso contrario
        '''
        
        return self.dados == []
    
    def empilhe(self,item):
        '''(Pilha) -> (None)

        Recebe uma referencia `self` a um objeto da classe Pilha e um item e
        adiciona este item ao topo da Pilha
        '''
        
        self.dados.append(item)
        return None
    
    def topo(self):
        '''(Pilha) -> (item)

        Recebe uma referencia `self` a um objeto da classe Pilha e
        retorna o item que se encontra no topo
        '''
        
        return self.dados[len(self.dados)-1]
    
    def __len__(self):
        '''(Pilha) -> (int)

        Recebe uma referencia `self` a um objeto da classe Pilha e
        retorna o número de itens da pilha
        '''
        
        return len(self.dados)
    
    def desempilhe(self):
        '''(Pilha) -> (None)

        Recebe uma referencia `self` a um objeto da classe Pilha e
        remove o item do topo da Pilha
        '''
        
        item = self.dados[len(self.dados)-1]
        self.dados.pop()
        return item
    
    def __eq__(self,other):
        '''(Pilha, Pilha) -> bool
        
        Retorna a comparação da Pilha `self` com a Pilha `other`.
        Usado pelo Python quando escrevemos Pilha == Pilha
        '''
        
        if self.dados == other.dados:
            return True
        else:
            return False
    
    

## ==================================================================
## Escreva outras funções e classes caso desejar

def testes():

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")
    
def main():
    print('Teste realizado \t\t\t Resultado esperado')
    print(f'palindromo(123) = {palindromo(123)}\t\t False')
    print(f'palindromo("acaxi") = {palindromo("abacaxi")}\t False')
    print(f'palindromo(159951) = {palindromo(159951)}\t True')
    print(f'palindromo("Arara") = {palindromo("arara")}\t True')
    print(f'palindromo("Aérea") = {palindromo("Aérea")}\t True')
    print(f'palindromo("") = {palindromo("")}\t\t True')
    print(f'palindromo(0) = {palindromo(0)}\t\t True')
    print(f'palindromo("afã.") = {palindromo("afã.")}\t\t True')
    print(f'palindromo("Socorram-me subi no onibus em Marrocos") = {palindromo("Socorram-me subi no onibus em Marrocos")}\t\t True')

    
    
    
## ==================================================================
if __name__ == '__main__':
    main()

