numero = int(input("digite o numero que quer ver a tabuada: "))
for x in range (0,11,1):
    resultado  = numero * x
    print("o resultado de {} x {} é {}".format(numero, x, resultado))