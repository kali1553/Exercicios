res = input("\nDeseja converter uma temperatura em graus Celsius para Farenheit ou vice-versa? S/N: ")
if res == 'S' or res == 's':
    def Celsius_para_Farenheit(celsius):
        return celsius * (9 / 5) + 32
    def Farenheit_para_Celsius(farenheit):
        return (farenheit - 32) * 5 / 9
    def escolhaConversão():
        opção = input("\nDigite:\n1 - Celsius para Farenheit\n2 - Farenheit para Celsius\n")
        if opção == '1':
            temperatura = float(input("\nDigite a temperatura: "))
            return Celsius_para_Farenheit(temperatura)
        elif opção == '2':
            temperatura = float(input("\nDigite a temperatura: "))
            return Farenheit_para_Celsius(temperatura)
    print(escolhaConversão())
else:
    print("\nTenha um bom dia!\n")