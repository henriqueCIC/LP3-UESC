class Lampada:
    def __init__(self):
        self.estado = "apagada"

    def acende(self):
        if self.estado == "apagada":
            self.estado = "acesa"
            print("A lâmpada foi acesa.")
        elif self.estado == "meia-luz":
            self.estado = "acesa"
            print("A lâmpada foi acesa.")
        else:
            print("A lâmpada já está acesa.")

    def apaga(self):
        if self.estado == "acesa":
            self.estado = "apagada"
            print("A lâmpada foi apagada.")
        elif self.estado == "meia-luz":
            self.estado = "apagada"
            print("A lâmpada foi apagada.")
        else:
            print("A lâmpada já está apagada.")

    def meiaLuz(self):
        if self.estado == "apagada":
            self.estado = "meia-luz"
            print("A lâmpada está em meia-luz.")
        elif self.estado == "acesa":
            self.estado = "meia-luz"
            print("A lâmpada está em meia-luz.")
        else:
            print("A lâmpada já está em meia-luz.")

    def LampadaTresEstados(self, luminosidade):
        if luminosidade == 0:
            self.estado = "apagada"
        elif 0 < luminosidade < 100:
            self.estado = "meia-luz"
        elif luminosidade == 100:
            self.estado = "acesa"
        else:
            print("Luminosidade fora do intervalo (0 a 100).")

    def mostraEstado(self):
        print(f"O estado da lâmpada é: {self.estado}")

lampada = Lampada()
lampada.acende()
lampada.mostraEstado()
lampada.apaga()
lampada.mostraEstado()
lampada.meiaLuz()
lampada.mostraEstado()
