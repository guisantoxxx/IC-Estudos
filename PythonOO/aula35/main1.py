# importando classe de outro arquivo
from pessoa_modelo1 import Pessoa

# instanciando novas Pessoas a partir da classe
p1 = Pessoa('Guilherme', 20)
p2 = Pessoa('Júlia', 20)

p1.falar()
p1.comer()
p1.comer()

p2.pararComer()
p1.pararComer()