class Cliente:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []
    
    def insere_endereco(self, cidade, estado):
        # instancia um novo objeto para inserir na lista
        # assim, se apagar a classe Cliente, todas as instancias de Endereco serao apagadas, pois so sao instanciadas dentro da classe Cliente
        self.endereco.append(Endereco(cidade,estado))
        
    def lista_enderecos(self):
        for e in self.endereco:
            print(e.cidade, e.estado)
        
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado