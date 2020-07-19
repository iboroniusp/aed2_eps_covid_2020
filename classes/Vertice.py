class Vertice:
    def __init__(self, id):
        self.id = id
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)
            #self.vizinhos.sort()

