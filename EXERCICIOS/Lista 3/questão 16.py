class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

    def inicializaData(self, novoDia, novoMes, novoAno):
        if self.dataValida(novoDia, novoMes, novoAno):
            self.dia = novoDia
            self.mes = novoMes
            self.ano = novoAno
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

    def diaDaSemana(self):
        diaSemana = [
            "Domingo",
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
        ]
        diasPorMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        totalDias = 0
        for i in range(1, self.mes):
            totalDias += diasPorMes[i]
        totalDias += self.dia

        # 01/01/1900 considerei sendo um domingo
        diaSemanaI = (totalDias + 1) % 7

        return diaSemana[diaSemanaI]


def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    data = Data()
    data.inicializaData(dia, mes, ano)
    data.mostraData()

    if data.dataValida(data.dia, data.mes, data.ano):
        diaSemana = data.diaDaSemana()
        print(f"Data válida! Dia da semana: {diaSemana}")
    else:
        print("Data inválida.")


main()
