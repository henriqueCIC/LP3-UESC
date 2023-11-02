class Data:
    def __init__(self):
        self.__dia = 0
        self.__mes = 0
        self.__ano = 0

    def inicializarData(self, dia, mes, ano):
        if self.verificarData(dia, mes, ano):
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
            print("Data inicializada.")
        else:
            print("Data inválida. A data foi alterada.")
            self.__dia = 0
            self.__mes = 0
            self.__ano = 0

    def verificarData(self, dia, mes, ano):
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
        elif mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        return False

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        self.__dia = dia

    def getMes(self):
        return self.__mes

    def setMes(self, mes):
        self.__mes = mes

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getData(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

    def imprimirData(self):
        print(self.getData())
#
    def imprimirDataExtenso(self):
        meses = {
            1: "janeiro",
            2: "fevereiro",
            3: "março",
            4: "abril",
            5: "maio",
            6: "junho",
            7: "julho",
            8: "agosto",
            9: "setembro",
            10: "outubro",
            11: "novembro",
            12: "dezembro",
        }
        nome_mes = meses.get(self.__mes, "")
        print(f"{self.__dia} de {nome_mes} de {self.__ano}")

    def isPrevious(self, outraData):
        if self.__ano < outraData.getAno():
            return True
        elif self.__ano == outraData.getAno():
            if self.__mes < outraData.getMes():
                return True
            elif self.__mes == outraData.getMes():
                return self.__dia < outraData.getDia()
        return False

    def howManyDays(self, outraData):
        diaMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        totalDias = self.__dia
        for i in range(self.__mes - 1):
            totalDias += diaMes[i]
        totalDias += self.__ano * 365

        totalDiasOutra = outraData.getDia()
        for i in range(outraData.getMes() - 1):
            totalDiasOutra += diaMes[i]
        totalDiasOutra += outraData.getAno() * 365
        return totalDiasOutra - totalDias

    def dayOfWeek(self):
        diaMes = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        ano = self.__ano - (self.__mes < 3)
        dia_semana = (
            ano
            + ano // 4
            - ano // 100
            + ano // 400
            + diaMes[self.__mes - 1]
            + self.__dia
        ) % 7
        dias_da_semana = [
            "Domingo",
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
        ]
        return dias_da_semana[dia_semana]


def main():
    print("Primeira Data:")
    dia1 = int(input("Digite o dia: "))
    mes1 = int(input("Digite o mês: "))
    ano1 = int(input("Digite o ano: "))
    print("Segunda Data:")
    dia2 = int(input("Digite o dia: "))
    mes2 = int(input("Digite o mês: "))
    ano2 = int(input("Digite o ano: "))

    data1 = Data()
    data1.inicializarData(dia1, mes1, ano1)
    data2 = Data()
    data2.inicializarData(dia2, mes2, ano2)

    if data1.verificarData(dia1, mes1, ano1) and data2.verificarData(dia2, mes2, ano2):
        print("Data 1:")
        data1.imprimirData()
        print("Data 2:")
        data2.imprimirData()
        print("Diferença de dias entre as datas:", data1.howManyDays(data2))
        print("Data 1 é anterior a Data 2?", data1.isPrevious(data2))
        print("Data 2 é anterior a Data 1?", data2.isPrevious(data1))
        print("Dia da semana de Data 1:", data1.dayOfWeek())
        print("Dia da semana de Data 2:", data2.dayOfWeek())
    else:
        print("Pelo menos uma das datas é inválida.")


if __name__ == "__main__":
    main()
