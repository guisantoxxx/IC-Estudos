class Escritor:
    def __init__(self, nome):
        # atributo privado,com __ antes do nome
        self.__nome = nome
        # ferramenta podera receber certos objetos instanciiados, caneta,maquina de escrever, etc
        self.__ferramenta = None
    
    #Getter
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
        
    @property
    
    def marca(self):
        return self.__marca
    
class MaquinaDeEscrever:
    
    def escrever(self):
        print('Maquina escrevendo...')