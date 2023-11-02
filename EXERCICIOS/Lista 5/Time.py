class TempoConvencional:
    def __init__(self, hora, min, seg):
        self.hora = hora
        self.min = min
        self.seg = seg

    def validateTime(self, hora, min, seg):
        return self.validHour(hora) and self.validMinOrSec(min) and self.validMinOrSec(seg)

    def validHour(self, hora):
        return 0 <= hora < 25

    def validMinOrSec(self, segundo):
        return 0 <= segundo < 61

    def setTime(self, hora, min, seg):
        if self.validateTime(hora, min, seg):
            self.hora = hora
            self.min = min
            self.seg = seg
        else:
            self.hora = 0
            self.min = 0
            self.seg = 0

    def getTime(self):
        return f"{self.hora}:{self.min}:{self.seg}"

    def prnTime(self):
        print(self.getTime())

    def isAm(self):
        return self.hora < 12

    def cron(self, outraHora):
        segundosAtual = self.hora * 3600 + self.min * 60 + self.seg #converte
        segundosOutro = outraHora.hora * 3600 + outraHora.min * 60 + outraHora.seg
        if outraHora.hora < self.hora:  # considera que outraHora é do dia seguinte
            segundosOutro += 24 * 3600
        return segundosOutro - segundosAtual

    def addSeconds(self, secs):
        total_segundos = self.hora * 3600 + self.min * 60 + self.seg + secs
        self.hora = total_segundos // 3600
        total_segundos %= 3600
        self.min = total_segundos // 60
        self.seg = total_segundos % 60

tempo1 = TempoConvencional(10, 30, 45)
tempo2 = TempoConvencional(13, 30, 30)
print("É AM TEMPO1:", tempo1.isAm())
print("É AM TEMPO2:", tempo2.isAm())

print("\nSegundos entre tempo1 até tempo2:", tempo1.cron(tempo2))

print("tempo1 + 5000segundos")
tempo1.addSeconds(5000)
tempo1.prnTime()
