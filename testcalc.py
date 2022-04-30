# importar funções de calculo:
import calc
from calc import soma, subtrair, multiplicar

# solicitar valores ao usuário:
valor1 = input("digite um valor: ")
valor2 = input("digite outro valor: ")

# armazenando a soma:
somar = calc.soma(valor1, valor2)
subtração = subtrair(valor1, valor2)
multiplicação = multiplicar(valor1, valor2)

# exibir a soma:
print("\nA soma dos valores é {}".format(somar))
print("\nA subtração dos valores é {}".format(subtração))
print("\nA multiplicação dos valores é {}".format(multiplicação))