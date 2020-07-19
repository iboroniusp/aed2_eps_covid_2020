# Descricao: Este codigo ira formular um grafo em lista de adjacencia a fim de
# representar conexoes entre os individuos entrevistados na pequisa Origem-Destino.
# O cenario escolhido e o cenario 3, onde apenas serviços essenciais estão abertos.

from classes.Grafo import Grafo
from datetime import datetime
import matplotlib.pyplot as plt

cenario3_file = 'dados/cenario3.txt'

start_execucao = datetime.now()

with open(cenario3_file) as file:
    num_vertices = int(file.readline())
    num_arestas = int(file.readline())
    arestas = file.readlines()

grafo = Grafo(num_vertices)
for aresta in arestas:
    aresta_list = aresta.split(' ')
    v1 = int(aresta_list[0])
    v2 = int(aresta_list[1])
    grafo.add_aresta(v1, v2)

graus = grafo.get_graus()
grau_maximo = max(graus)
print("Arestas inseridas:", grafo.num_arestas)
print("Grau máximo:", grau_maximo)

# Plotagem do histograma
plt.style.use('ggplot')
plt.hist(graus, bins=10)
plt.title("Frequência dos graus dos nós para o cenário 3")
plt.show()

end_execucao = datetime.now()
runtime_execucao = (end_execucao - start_execucao).total_seconds() / 60
print(f'Program runtime: {runtime_execucao} min')
