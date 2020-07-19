from classes.Vertice import Vertice


class Grafo:
    def __init__(self, num_vertices):
        self.vertices_dict = {}
        self.vertices_list = []
        self.vertices_ok_list = []
        self.num_arestas = 0
        self.num_vertices = num_vertices
        for i in range(1, num_vertices):
            self.add_vertice(i)

    # O metodo abaixo existe para que possamos inicializar um grafo de acordo com seus vertices
    # Não adicionamos vertices com id repetido
    def add_vertice(self, id):
        if id not in self.vertices_dict:
            vertice = Vertice(id)
            self.vertices_dict[vertice.id] = vertice
            self.vertices_list.append(vertice)
            return True
        else:
            return False

    # Criamos o método para adicionar vertice conectado e neste caso so existiram vertices que possuem arestas
    # Não adicionamos vertices com id repetido
    def add_vertice_conectado(self, id):
        if id in self.vertices_dict:
            self.vertices_ok_list.append(self.vertices_dict[id])
            return True
        else:
            return False

    def add_aresta(self, a_id, b_id):
        a = self.vertices_dict[a_id]
        b = self.vertices_dict[b_id]
        if a and b:
            a.adicionar_vizinho(b)
            b.adicionar_vizinho(a)
            print(f"Aresta adicionada entre {a_id} e {b_id}")
            self.num_arestas += 1
            return True
        else:
            return False

    def gerar_txt_arestas(self):
        arquivo_saida = open('Saida.txt', 'a')
        for key in sorted(list(self.vertices_dict.keys())):
            txt_linha = f'{key}: {len(self.vertices_dict[key].vizinhos)}\n'
            arquivo_saida.write(txt_linha)
        arquivo_saida.close()

    def get_graus(self):
        graus = []
        for v in self.vertices_list:
            grau_vertice = len(v.vizinhos)
            if grau_vertice != 0:
                graus.append(grau_vertice)
        return graus
