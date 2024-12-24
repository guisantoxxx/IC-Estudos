class Pessoa:
    ano_atual = 2024
    
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    # cls se refere à classe e não a instancia
    # por passar cls ao inves de self, faz referencia ao atributo da classe,e nao da instancia
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        # cls se refere ao atributo da classe
        idade = cls.ano_atual - ano_nascimento
        
        # ao retornar cls(), esta instanciando e retornando uma nova classe
        return cls(nome, idade)
        

p1 = Pessoa ('Guilherme', 20)
print(Pessoa.ano_atual)

# nesse caso, estou usando um metodo de classe para instancias um novo objeto
p2 = Pessoa.por_ano_de_nascimento('Júlia', 2004)
print(p2.nome,p2.idade)