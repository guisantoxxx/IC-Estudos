class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/ 100))
    
    @property
    def nome(self):
        return self._nome
    
    #  o setter sempre faz uma verificacao antes de definir o valor do atributo
    @nome.setter
    def nome(self, valor):
        valor = str.lower(valor)
        self._nome = valor
        
    # Getter
    @property
    def preco(self):
        # o _preco, com _ antes do nome, é dado por convenção,_ antes do nome do atributo 
        return self._preco
    
    # Setter, é chamado quando é atribuido um valor para preco la embaixo
    @preco.setter
    def preco(self, valor):
        # checa se o valor éuma instancia de str
        if isinstance(valor,str):
            # substitui R$ por nada,o removendo
            valor =valor.replace('R$', '')
            valor = float(valor)
            
        self._preco = valor
        

p1 = Produto('CAMISETA', 100)
p1.desconto(10)
print(p1.preco)
print(p1.nome)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.preco)
print(p2.nome)
