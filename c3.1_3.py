#algoritmo para verificar se um número é divisível por 2

valor = 1

while valor %2 == 1:
    valor = int(input("Digite um número par: "))
print("\n\nvocê digitou {} que é um número par.\nParabéns".format(valor))