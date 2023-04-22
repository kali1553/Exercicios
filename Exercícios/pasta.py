file = open(r"C:\Users\Pedro\OneDrive\Documentos\TXT\numeros.txt", "r").read().split("\n")

def é_primo(n):
    if int(n) == 0 or n == 1:
        return False
    for i in n:
        if int(n) % int(i) == 0:
            return False
    return True

par = 0
impar = 0
primo = 0

for i in file:
    if é_primo(i):
        primo +=1
    if int(i) == 2:
        primo+=1
        par+=1
    if int(i) % 2 !=0:
        impar+=1    
    if int(i) % 2 == 0:
        par+=1

new = open(r"C:\Users\Pedro\OneDrive\Documentos\TXT\relatorio.txt", "w")

new.write("*********************************************************\n")
new.write("Relatório\n")
new.write("*********************************************************\n")
new.write('Qtd números pares:' + str(par)+"\n")
new.write('Qtd números impares:' + str(impar)+"\n")
new.write('Qts números primos:' + str(primo)+"\n")
new.write("*********************************************************")
new.close()

#programa para contar o numero de primos, pares e impares e escrever em um relatório num arquivo txt