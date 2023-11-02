import math

class Ponto2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def imprimirPonto(self):
        print(f"Ponto: ({self.x}, {self.y})")

    def EixoX(self):
        return self.y == 0

    def EixoY(self):
        return self.x == 0

    def Eixos(self):
        return self.x == 0 and self.y == 0

    def quadrante(self):
        if self.Eixos():
            return 0
        elif self.x > 0:
            if self.y > 0:
                return 1
            else:
                return 4
        else:
            if self.y > 0:
                return 2
            else:
                return 3

    def distancia(self, outroPonto):
        difX = self.x - outroPonto.x
        difY = self.y - outroPonto.y
        return math.sqrt(difX * difX + difY * difY)

ponto1 = Ponto2D(0, 3)
ponto2 = Ponto2D(10, 0)
ponto1.imprimirPonto()
ponto2.imprimirPonto()

distancia = ponto1.distancia(ponto2)
print(f"A distância entre os pontos é {distancia}")
print(f"Ponto1 está no eixo X: {ponto1.EixoX()}\nPonto1 está no eixo Y: {ponto1.EixoY()}\nPonto1 está sobre os eixos: {ponto1.Eixos()}")
print(f"Ponto2 está no eixo X: {ponto2.EixoX()}\nPonto2 está no eixo Y: {ponto2.EixoY()}\nPonto2 está sobre os eixos: {ponto2.Eixos()}")
print(f"Quadrante: {ponto1.quadrante()}")
print(f"Quadrante: {ponto2.quadrante()}")
