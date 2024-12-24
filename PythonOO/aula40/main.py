class BaseDeDados:
    def __init__(self):
        # atributo com _ antes do nome é dado como privado, mas nada é bloqueado
        # atributos com __ antes do nome,proibem o acesso a atributos e metodos
        self.__dados = {}
        
    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def listaClientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]
        
bd = BaseDeDados()
bd.inserirCliente(1, 'Gui1')
bd.inserirCliente(2, 'Gui2')
bd.inserirCliente(3, 'Gui3')

bd.listaClientes()

