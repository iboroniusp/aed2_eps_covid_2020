class Vertice:
    def __init__(self, id):
        self.id = id
        self.situacao = 'S'
        # Aqui o valor inicial do atributo situacao e 'S' de Suscetivel, por conta da
        # inicializacao do modelo de contagio SIR
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho):
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)
            #self.vizinhos.sort()

