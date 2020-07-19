# Descricao: Este codigo ira simular o modelo de contagio SIR simples.
# Utilizaremos um grafo em lista de adjacencia a fim de representar a componente gigante do grafo
# O cenario escolhido e o cenario 3, onde apenas serviços essenciais estão abertos.
# Apesar de existirem 86318 vertices, nem todos estão conectados entre si, por isso, calculamos também os vertices validos

from classes.Grafo import Grafo
from datetime import datetime
from random import random, choice
import matplotlib.pyplot as plt

gigante3_file = 'dados/gigante3.txt'
start_execucao = datetime.now()

with open(gigante3_file) as file:
    num_vertices = int(file.readline())
    num_arestas = int(file.readline())
    arestas = file.readlines()

grafo = Grafo(num_vertices)
for aresta in arestas:
    aresta_list = aresta.split(' ')
    v1 = int(aresta_list[0])
    v2 = int(aresta_list[1])
    grafo.add_vertice_conectado(v1)
    grafo.add_vertice_conectado(v2)
    grafo.add_aresta(v1, v2)


def simulaSIR(c, r):
    print(f"\n>> MODELO DE CONTAGIO SIR PARA c={c} e r={r}")
    # Abaixo vamos sortear um elemento da lista de vertices validos do grafo para ser o primeiro paciente infectado
    paciente_zero = choice(grafo.vertices_ok_list)
    paciente_zero.situacao = 'I'
    print("PACIENTE ZERO:", paciente_zero.id, paciente_zero.situacao)
    # Vamos separar os vertices infectados, recuperados e suscetiveis
    suscetiveis = grafo.vertices_ok_list
    suscetiveis.pop(suscetiveis.index(paciente_zero))
    # Os suscetiveis são todos com excecao do primeiro paciente infectado

    infectados = [paciente_zero]
    recuperados = []

    # Este modelo seguirá executando até que não tenhamos mais nenhum infectado
    passo = 0
    while len(infectados) != 0:
        print("PASSO:", passo, "INFECTADOS:", len(infectados), "RECUPERADOS:", len(recuperados), "SUSCETIVEIS:", len(suscetiveis))
        for v in infectados:
            x = random()
            if x <= r:
                v.situacao = 'R'
                infectados.pop(infectados.index(v))
                recuperados.append(v)
                # Tiramos o recuperado da lista de infectados
            else:
                for w in v.vizinhos:
                    if w.situacao == 'S':
                        y = random()
                        if y <= c:
                            w.situacao = 'I'
                            suscetiveis.pop(suscetiveis.index(w))
                            infectados.append(w)
        passo += 1




    #imprimir um grafico onde x = numero de iteracoes do algoritmo
    # y=numero infectados
    # fazer um grafico de barras empilhadas com o numero de ifnectados em baixo e de recuperados em cims


# Abaixo chamamos a função de simulacao do SIR onde os parâmetros são (c, r)
# Lembrando que c = probabilidade de contagio e r = probabilidade de recuperacao
# Esses numeros foram escolhidos imaginando cenarios proximos aos reais, onde apesar da
# probabilidade de contagio ser grande, a probabilidade de recuperacao e maior

simulaSIR(0.5, 0.2)
simulaSIR(0.6, 0.6)
simulaSIR(0.4, 0.8)

end_execucao = datetime.now()
runtime_execucao = (end_execucao - start_execucao).total_seconds() / 60
print(f'Program runtime: {runtime_execucao} min')
