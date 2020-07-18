class Local:
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.frequentadores = list()

    def adicionar_frequentador(self, frequentador):
        if frequentador not in self.frequentadores:
            self.frequentadores.append(frequentador)


# pessoas entrevistadas na origem e destino = elas são os nós
# passando pela lista de frequentadores de um local, cria-se as arestas

