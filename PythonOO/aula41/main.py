from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

e1 = Escritor('Gui')
e2 = Escritor('Ju')
c1 = Caneta('Bic')
m1 = MaquinaDeEscrever()

e1.ferramenta = Caneta('Faber Castell')
e2.ferramenta =m1

e2.ferramenta.escrever()
print(e1.ferramenta.marca)