dataNascimento = input ("Digite a data de nascimento: ").split()
dataAtual = input ("Digite a data atual: ").split()

for y in dataNascimento:
    y = str(y)
    for k in y:
        metadeD1 = y[:2]
        metadeD2 = y[3:5]
        metadeD3 = y[6:]
        metadeD1 = int(metadeD1)
        metadeD2 = int(metadeD2)
        metadeD3 = int(metadeD3)

for y in dataAtual:
    y = str(y)
    for k in y:
        metade1 = y[:2]
        metade2 = y[3:5]
        metade3 = y[6:]
        metade1 = int(metade1)
        metade2 = int(metade2)
        metade3 = int(metade3)

dias =  metade1 - metadeD1
meses = metade2 - metadeD2
anos =  metade3 - metadeD3

dias += meses * 30 + anos * 365
meses += anos * 12

print("Dias:", dias, "\nMeses:", meses, "\nAnos:", anos)