#HENRIQUE BARRETO PEREIRA
class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

    def inicializaData(self, novo_dia, novo_mes, novo_ano):
        if self.dataValida(novo_dia, novo_mes, novo_ano):
            self.dia = novo_dia
            self.mes = novo_mes
            self.ano = novo_ano
            print("Data inicializada.")
        else:
            print("Data inválida. A data foi alterada.")
            self.dia = 0
            self.mes = 0
            self.ano = 0

    def dataValida(self, dia, mes, ano):   
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
        elif mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        else:
            return False

    def mostraData(self):
        print(f"Data: {self.dia}/{self.mes}/{self.ano}")

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    data = Data()
    data.inicializaData(dia, mes, ano)
    data.mostraData()

    if data.dataValida(data.dia, data.mes, data.ano):
        print("Data válida!!!")
    else:
        print("Data inválida.")

main()
