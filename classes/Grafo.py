from classes.Vertice import Vertice


class Grafo:
    def __init__(self, num_vertices):
        self.vertices_dict = {}
        self.vertices_list = []
        self.num_vertices = num_vertices
        for i in range(1, num_vertices):
            self.adicionar_vertice(Vertice(i))

    def adicionar_vertice(self, vertice):
        if vertice.id not in self.vertices_dict:
            self.vertices_dict[vertice.id] = vertice
            self.vertices_list.append(vertice)
            return True
        else:
            return False

    def adicionar_aresta(self, a_id, b_id):
        a = self.vertices_dict[a_id]
        b = self.vertices_dict[b_id]
        if a and b:
            a.adicionar_vizinho(b)
            b.adicionar_vizinho(a)
            print(f"Aresta adicionada entre {a_id} e {b_id}")
            return True
        else:
            return False

    def gerar_txt_arestas(self):
        arquivo_saida = open('Saida.txt', 'a')
        for key in sorted(list(self.vertices_dict.keys())):
            txt_linha = f'{key}: {len(self.vertices_dict[key].vizinhos)}\n'
            arquivo_saida.write(txt_linha)
        arquivo_saida.close()

    def get_grau_maximo(self):
        grau_maximo = 0
        for vertice in self.vertices_list:
            grau_vertice = len(vertice.vizinhos)
            if grau_vertice > grau_maximo:
                grau_maximo = grau_vertice
        return grau_maximo
