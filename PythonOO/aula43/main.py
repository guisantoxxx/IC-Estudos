from classes import Cliente, Endereco

c1 = Cliente('Gui', 20)
c1.insere_endereco('Sorocaba', 'SP')
c1.insere_endereco('Si', 'SP')

c2 = Cliente('Ju', 20)
c2.insere_endereco('Si', 'SP')

c1.lista_enderecos()