class Pessoa:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade 
        
    def falar(self):
        print('Falando ...')

# ao colocar Pessoa nos parenteses da classe, esta definido que as classes herdam Pessoa, seus atributos e metodos
class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass