from classes import Produto, CarrinhoDeCompras

c1 = CarrinhoDeCompras()
p1 = Produto('camisa', 50)
p2 = Produto('bermuda', 40)

c1.inserir_produto(p1)
c1.inserir_produto(p2)

c1.lista_produtos()
c1.soma_total()