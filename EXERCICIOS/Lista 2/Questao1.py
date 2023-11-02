import math
tot = 0
medida = [0] * 10
for i in range(10):
    medida[i] = float(input(f"medida {i}: "))
    tot += medida[i]
resultado = tot / len(medida)
varianc = sum((x - resultado) ** 2 for x in medida) / len(medida)
media = math.sqrt(varianc)
print("Média:", resultado)
print("DesvPad:", media)

if media > resultado * 0.1:
    print("O multimetro está com defeito")
else:
    print("O multimetro está aferido corretamente")
