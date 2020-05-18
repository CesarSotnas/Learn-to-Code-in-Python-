from calc import Calculadora

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

calculadora = Calculadora(valor1, valor2)

print("Qual operação deseja fazer?")
print("(1) Soma (2) Subtração (3) Multiplicação (4) Divisão")
indicador = int(input(""))


if indicador == 1:
    print(calculadora.soma)

elif indicador == 2:
   print(calculadora.subtracao)

elif indicador == 3:
   print(calculadora.multiplicacao)

elif indicador == 4:
   print(calculadora.divisao)

else:
    print("Opção inválida")

