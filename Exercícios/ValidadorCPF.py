CPF = input("Digite o CPF sem os pontos e sem o dígito: ")
def isCPF(string):
    cpf = list(map(int, string))
    cpfTrue = ''
    posição = 0
    for y in CPF:
        if posição % 3 == 0 and posição != 9 and posição != 0:
            cpfTrue += "."
        elif posição == 9:
            cpfTrue+="-"
        cpfTrue += y
        posição +=1
    print(cpfTrue)

    if len(cpf) == 11 and cpf.count(cpf[0]) != len(cpf):
        Decrescente = [i for i in range(10, 1, -1)]
        soma = 0
        for i, n in zip(cpf, Decrescente):
            soma += i * n
        if 11 - (soma % 11) == cpf[-2] or (11 - (soma % 11) >= 10 and cpf[-2] == 0):
            Decrescente.insert(0, 11)
            soma = 0
            for i, n in zip(cpf, Decrescente):
                soma += i * n
            if 11 - (soma % 11) == cpf[-1] or (11 - (soma % 11) >= 10 and cpf[-1] == 0):
                return True
    return False
print(isCPF(CPF))