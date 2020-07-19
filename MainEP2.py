# Descricao: Este codigo ira formular um grafo em lista de adjacencia a fim de
# representar conexoes entre os individuos entrevistados na pequisa Origem-Destino.
# O cenario escolhido e o cenario 3, onde apenas serviços essenciais estão abertos.

from classes.Grafo import Grafo
from datetime import datetime

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
    grafo.adicionar_aresta(v1, v2)

grau_maximo = grafo.get_grau_maximo()
print("Grau máximo:", grau_maximo)

graus = []
for i in range(grau_maximo+1):
    graus.append(0)

print(len(grafo.vertices_list))

for v in grafo.vertices_list:
    grau_vertice = len(v.vizinhos)
    print(grau_vertice)
    graus[grau_vertice] = graus[grau_vertice] + 1

for grau in graus:
    if grau == 98:
        print(graus.index(grau))

# cont_locais = 1
# arquivo_locais = open('Locais.txt', 'a')
# start_grafo = datetime.now()
# for local in locais_list:
#     txt_local_linha = f'Local: {cont_locais} ({local.coordenada_x}, {local.coordenada_y} | N. frequentadores: {len(local.frequentadores)}\n'
#     arquivo_locais.write(txt_local_linha)
#     for frequentador in local.frequentadores:
#         for proximo_frequentador in local.frequentadores:
#             if frequentador != proximo_frequentador:
#                 grafo.adicionar_vertice(frequentador)
#                 grafo.adicionar_vertice(proximo_frequentador)
#                 grafo.adicionar_aresta(frequentador, proximo_frequentador)
#     cont_locais += 1
# arquivo_locais.close()
# grafo.gerar_txt_arestas()
# end_grafo = datetime.now()
# runtime_grafo = (end_grafo - start_grafo).total_seconds() / 60
# print(f'Grafo runtime: {runtime_grafo} min')

end_execucao = datetime.now()
runtime_execucao = (end_execucao - start_execucao).total_seconds() / 60
print(f'Program runtime: {runtime_execucao} min')
