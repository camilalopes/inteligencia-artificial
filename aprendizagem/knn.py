class Knn():
    k = 1

    def __init__(self, k):
        self.k = k

    def calcula_distancia(self, vetor_1, vetor_2) -> float:
        distancia = 0.0
        for i in range(len(vetor_1)):
            distancia += (vetor_1[i] - vetor_2[i]) ** 2
        return distancia ** (1/2)

    def get_vizinhos(self, centro_consulta, elementos) -> list:
        vizinhos: list = []
        k_vizinhos: list = []
        for elem in elementos:
            distancia = self.calcula_distancia(centro_consulta, elem)
            vizinhos.append([distancia, elem])
        vizinhos.sort(key=self.retorna_distancia)

        for i in range(self.k):
            k_vizinhos.append(vizinhos[i][1])

        return k_vizinhos

    def retorna_distancia(self, elemento) -> float:
        return elemento[0]
