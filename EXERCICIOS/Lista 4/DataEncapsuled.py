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
        12: "dezembro"
    }
    nome_mes = meses.get(self.__mes, "")
    print(f"{self.__dia} de {nome_mes} de {self.__ano}")


def main():
  dia = int(input("Digite o dia: "))
  mes = int(input("Digite o mês: "))
  ano = int(input("Digite o ano: "))
  data = Data()
  data.inicializarData(dia, mes, ano)
  data.imprimirData()
  data.imprimirDataExtenso()

  if data.verificarData(data.getDia(), data.getMes(), data.getAno()):
    print("Data válida!!!")
  else:
    print("Data inválida.")


main()
