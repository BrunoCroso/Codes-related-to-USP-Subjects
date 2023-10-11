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
        - Não foram utilizadas fontes externas para este trabalho

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - Não tive auxílio na realização deste trabalho
'''


def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')

class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    
    def __init__(self,horas = 0,minutos = 0,segundos = 0):
        '''(Horario, int, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros segundos, minutos e horas
        que representam, respectivamente, os segundos, minutos e horas
        que representam o horario
        '''
        
        if segundos >= 60:
            minutos += segundos // 60
            segundos = segundos % 60
        if minutos >= 60:
            horas += minutos // 60
            minutos = minutos % 60
        while horas >= 24:
            horas -= 24
        

        self.seg = segundos
        self.min = minutos
        self.horas = horas
        self.dados = [segundos,minutos,horas]
        
    def __str__(self):
        '''(Horario) -> str

        Recebe uma referencia `self` a um objeto da classe Horario e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  
        '''
        if self.horas < 10:
            horas = '0' + str(self.horas)
        else:
            horas = self.horas
        
        if self.min < 10:
            minutos = '0' + str(self.min)
        else:
            minutos = self.min
        
        if self.seg < 10:
            segundos ='0' + str(self.seg)
        else:
            segundos = self.seg
            
            
        return (f'{horas}:{minutos}:{segundos}')
        
    def __add__(self, other):
        """ (Horario, Horario) -> Horario

        Retorna a soma do Horario `self` e do Horario `other`.
        Usado pelo Python quando escrevemos Horario + Horario
        
        """
        segundos = self.seg + other.seg
        minutos = self.min + other.min
        horas = self.horas + other.horas
        
        if segundos >= 60:
            minutos += segundos // 60
            segundos = segundos % 60
        if minutos >= 60:
            horas += minutos // 60
            minutos = minutos % 60
        while horas >= 24:
            horas -= 24
            
        return Horario(horas,minutos,segundos)

    
    def __sub__(self,other):
        """ (Horario, Horario) -> Horario

        Retorna a subtração do Horario `self` e do Horario `other`.
        Usado pelo Python quando escrevemos Horario - Horario
        
        """        
        
        segundos = self.seg - other.seg
        minutos = self.min - other.min
        horas = self.horas - other.horas        
        
        while segundos < 0:
            segundos += 60
            minutos -= 1
            
        while minutos < 0:
            minutos += 60
            horas -= 1
            
        if horas < 0:
            horas = 0
            minutos = 0
            segundos = 0
    
        return Horario(horas,minutos,segundos)

    
    def __lt__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario < Horario
        '''
        
        if self.horas < other.horas:
            return True
        elif self.horas > other.horas:
            return False
        elif self.horas == other.horas:
            
            if self.min < other.min:
                return True
            elif self.min > other.min:
                return False
            elif self.min == other.min:
                
                if self.seg < other.seg:
                    return True
                elif self.seg > other.seg:
                    return False         
                elif self.seg == other.seg:
                    return False


    def __le__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario <= Horario
        '''
        
        if self.horas < other.horas:
            return True
        elif self.horas > other.horas:
            return False
        elif self.horas == other.horas:
            
            if self.min < other.min:
                return True
            elif self.min > other.min:
                return False
            elif self.min == other.min:
                
                if self.seg < other.seg:
                    return True
                elif self.seg > other.seg:
                    return False         
                elif self.seg == other.seg:
                    return True



    def __eq__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario == Horario
        '''

        if self.dados == other.dados:
            return True
        else:
            return False
        
    
    def __ne__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario != Horario
        '''

        if self.dados == other.dados:
            return False
        else:
            return True
    
    
    def __gt__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario > Horario
        '''
        
        if self.horas > other.horas:
            return True
        elif self.horas < other.horas:
            return False
        elif self.horas == other.horas:
            
            if self.min > other.min:
                return True
            elif self.min < other.min:
                return False
            elif self.min == other.min:
                
                if self.seg > other.seg:
                    return True
                elif self.seg < other.seg:
                    return False         
                elif self.seg == other.seg:
                    return False
    
    
    def __ge__(self,other):
        '''(Horario, Horario) -> bool
        
        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario >= Horario
        '''

        if self.horas > other.horas:
            return True
        elif self.horas < other.horas:
            return False
        elif self.horas == other.horas:
            
            if self.min > other.min:
                return True
            elif self.min < other.min:
                return False
            elif self.min == other.min:
                
                if self.seg > other.seg:
                    return True
                elif self.seg < other.seg:
                    return False         
                elif self.seg == other.seg:
                    return True
    


if __name__ == '__main__':
     main()

