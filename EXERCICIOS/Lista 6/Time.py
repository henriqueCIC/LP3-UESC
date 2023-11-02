class TempoConvencional:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    def __init__(self, hora):
        self.hora = hora
        self.minuto = 0
        self.segundo = 0

    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
        self.segundo= 0

    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo= segundo    

    def __init__(self, time):
        self.hora = time.hora
        self.time.minuto = time.minuto
        self.time.segundo= time.segundo 

    def validateTime(self, hora, minuto, segundo):
        return self.validHour(hora) and self.validMinOrSec(minuto) and self.validMinOrSec(segundo)

    def validHour(self, hora):
        return 0 <= hora < 24

    def validMinOrSec(self, valor):
        return 0 <= valor < 60

    def setTime(self, hora, minuto, segundo):
        if self.validateTime(hora, minuto, segundo):
            self.hora = hora
            self.minuto = minuto
            self.segundo = segundo
        else:
            print("Horário inválido.")

    def getTime(self):
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"

    def prnTime(self):
        print(self.getTime())

    def isAm(self):
        return self.hora < 12

    def cron(self, outraHora):
        segundosAtual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundosOutro = outraHora.hora * 3600 + outraHora.minuto * 60 + outraHora.segundo
        if outraHora.hora < self.hora:
            segundosOutro += 24 * 3600
        return segundosOutro - segundosAtual

    def addTime(self, horas=0, minutos=0, segundos=0):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos + minutos * 60 + horas * 3600
        self.hora = total_segundos // 3600
        total_segundos %= 3600
        self.minuto = total_segundos // 60
        self.segundo = total_segundos % 60

    def addTimeObj(self, outroTempo):
        self.addTime(outroTempo.hora, outroTempo.minuto, outroTempo.segundo)


tempo10 = TempoConvencional(10, 30, 45)
tempo20 = TempoConvencional(13, 30, 30)

print("É AM TEMPO10:", tempo10.isAm())
print("É AM TEMPO20:", tempo20.isAm())

print("\nSegundos entre tempo10 até tempo20:", tempo10.cron(tempo20))

print("tempo10 + 5000 segundos")
tempo10.addTime(segundos=5000)
tempo10.prnTime()

print("tempo10 + 10 minutos e 5000 segundos")
tempo10.addTime(minutos=10, segundos=5000)
tempo10.prnTime()

print("tempo10 + 1 hora, 10 minutos e 5000 segundos")
tempo10.addTime(horas=1, minutos=10, segundos=5000)
tempo10.prnTime()

print("tempo10 adicionando tempo de tempo20")
tempo10.addTimeObj(tempo20)
tempo10.prnTime()






class TempoConvencional:
#LISTA06 CONSTRUTOR COM PARAMETRO 
    def __init__(self, hora, min, seg):
        self.hora = hora
        self.min = min
        self.seg = seg
#LISTA06 CONSTRUTOR SEM PARAMETRO
    def __init__(self):
      self.hora = 00
      self.min = 00
      self.seg = 00
tempo0 = TempoConvencional( 23, 59, 59)
print(tempo0) 

class TempoConvencional:
    def __init__(self, hora=0, min=0, seg=0):
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
        else: pass

    def getTime(self):
        return f"{self.hora}:{self.min}:{self.seg}"

    def prnTime(self):
        print(self.getTime())

    def isAm(self):
        return self.hora < 12

    def cron(self, outraHora):
        segundosAtual = self.hora * 3600 + self.min * 60 + self.seg 
        segundosOutro = outraHora.hora * 3600 + outraHora.min * 60 + outraHora.seg
        return segundosOutro - segundosAtual

    def addTime(self, h=0, m=0, s=0):
        total_segundos = self.hora * 3600 + self.min * 60 + self.seg + s + m * 60 + h * 3600
        self.hora = total_segundos // 3600
        total_segundos %= 3600
        self.min = total_segundos // 60
        self.seg = total_segundos % 60

    def addTimeObj(self, obj):
        self.addTime(obj.hora, obj.min, obj.seg)


tempo10 = TempoConvencional(10, 30, 45)
tempo20= TempoConvencional(13, 30, 20)
print("É AM TEMPO10:", tempo10.isAm())
print("É AM TEMPO20:", tempo20.isAm())

print("\nSegundos entre tempo10 até tempo20:", tempo10.cron(tempo20))

print("tempo10 + 5000segundos")
tempo10.addTime(s=5000)
tempo10.prnTime()

# Adicionando minutos e segundos
print("tempo10 + 10minutos e 5000segundos")
tempo10.addTime(m=10, s=5000)
tempo10.prnTime()

# Adicionando horas, minutos e segundos
print("tempo10 + 1hora, 10minutos e 5000segundos")
tempo10.addTime(h=1, m=10, s=5000)
tempo10.prnTime()

# Adicionando tempo de outro objeto
print("tempo10 adicionando tempo de tempo20")
tempo10.addTimeObj(tempo20)
tempo10.prnTime()

# Criando uma cópia de um objeto
tempo30 = tempo10
print("Objeto copiado:", tempo30.getTime())
#LISTA06 CONSTRUTOR COM PARAMETRO HORA
    def __init__(self, hora):
      self.hora = 'HH'
      self.min = 00
      self.seg = 00
tempo1 = TempoConvencional()
print(tempo1)
#LISTA06 CONSTRUTOR COM PARAMETRO HORA E MINUTO
    def __init__(self, hora, min):
      self.hora = 'HH'
      self.min = 'MM'
      self.seg = 00
tempo2 = TempoConvencional()
print(tempo2)
#LISTA06 CONSTRUTOR COM PARAMETRO HORA, MINUTO E SEGUNDO
    def __init__(self, hora, min, seg):
      self.hora = 'HH'
      self.min = 'MM'
      self.seg = 'SS'
tempo3 = TempoConvencional()
print(tempo3)
#FAZER ESSA " Construtor que recebe como parâmetro um objeto Time, e retorna um objeto
#idêntico ao parâmetro "






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
        else: pass
        

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

tempo10 = TempoConvencional(10, 30, 45)
tempo20= TempoConvencional(13, 30, 30)
print("É AM TEMPO10:", tempo1.isAm())
print("É AM TEMPO20:", tempo2.isAm())

print("\nSegundos entre tempo10 até tempo20:", tempo10.cron(tempo20))

print("tempo10 + 5000segundos")
tempo10.addSeconds(5000)
tempo10.prnTime()
