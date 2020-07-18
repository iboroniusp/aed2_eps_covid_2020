
class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice.id not in self.vertices:
            self.vertices[vertice.id] = vertice
            return True
        else:
            return False

    def adicionar_aresta(self, a, b):
        if a.id in self.vertices and b.id in self.vertices:
            a.adicionar_vizinho(b)
            b.adicionar_vizinho(a)
            return True
        else:
            return False

    def gerar_txt_arestas(self):
        arquivo_saida = open('Saida.txt', 'a')
        for key in sorted(list(self.vertices.keys())):
            txt_linha = f'{key}: {len(self.vertices[key].vizinhos)}\n'
            arquivo_saida.write(txt_linha)
        arquivo_saida.close()
