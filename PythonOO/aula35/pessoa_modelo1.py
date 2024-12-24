# molde da classe
class Pessoa:
    # self refere-se a própria istancia que estásendo chamado
    #def falar(self):
        #print('Pessoa está falando')
        
    # parametro self é enviado naturalmente pelo python,nao sendo preciso enviar manualmente
    # funcao __init__ é a funcao construtora da classe
    def __init__(self,nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo =comendo
        self.falando = falando
        
    def falar(self):
        print(f'Olá, meu nome é {self.nome}')
    
    def comer(self):
        if self.comendo:
            print('Já está comendo')
            return
        
        print(f'{self.nome} está comendo')
        self.comendo = True
        
    def pararComer(self):
        if(not self.comendo):
            print(f'{self.nome} não está comendo')
            return
        else:
            print(f'{self.nome} parou de comer')
            self.comendo = False