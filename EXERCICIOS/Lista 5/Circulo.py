import math

class Circulo:
    def __init__(self, posX, posY, raio):
        self.posX = posX
        self.posY = posY
        if self.valida_circulo(raio):
            self.raio = raio
        else:
            self.raio = 1.0
            print("Raio inválido")

    def set_posX(self, posX):
        self.posX = posX

    def set_posY(self, posY):
        self.posY = posY

    def set_raio(self, raio):
        if self.valida_circulo(raio):
            self.raio = raio
        else:
            print("Valor inválido")

    def get_raio(self):
        return self.raio

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def eh_maior_que(self, rnd):
        return self.area() > rnd.area()

    def eh_ponto_interno(self, ponto):
        dist = math.sqrt((ponto.get_x() - self.posX) ** 2 + (ponto.get_y() - self.posY) ** 2)
        return dist < self.raio

    def valida_circulo(self, raio):
        return raio > 0

class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, outro_ponto):
        difX = self.x - outro_ponto.get_x()
        difY = self.y - outro_ponto.get_y()
        return math.sqrt(difX ** 2 + difY ** 2)

ponto1 = Ponto2D(0, 3)
ponto2 = Ponto2D(10, 0)

circulo1 = Circulo(0, 0, 2)
circulo2 = Circulo(5, 5, 3)

print("Círculo 1:")
print(f"Área: {circulo1.area()}")
print(f"Perímetro: {circulo1.perimetro()}")
print(f"É maior que Círculo 2? {circulo1.eh_maior_que(circulo2)}")
print(f"O ponto (1, 7) está dentro do círculo? {circulo1.eh_ponto_interno(ponto1)}")

print("\nCírculo 2:")
print(f"Área: {circulo2.area()}")
print(f"Perímetro: {circulo2.perimetro()}")
print(f"É maior que Círculo 1? {circulo2.eh_maior_que(circulo1)}")
print(f"O ponto (11, 2) está dentro do círculo? {circulo2.eh_ponto_interno(ponto2)}")
