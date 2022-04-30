'''
valor=float(input("digite um valor:"))

if (valor>=20 and valor<=25):
    print("Valor correto")
else:
    print("valor errado")



lista = [0, 2, 4, 8, 16, 32, 64, 128]
print(len(lista))

op = -1
while op != 5:
    print("\nMenu do super programa")
    print("1-rodar cód 1")
    print("2-rodar cód 2")
    print("3-rodar cód 3")
    print("4-rodar cód 4")
    print("5-sair do programa")
    op = int(input("\nInforme sua opção: "))
    if op == 1:
        print("cód 1 rodando")
    elif op == 2:
        print("cód 2 rodando")
    elif op == 3:
        print("cód 3 rodando")
    elif op == 4:
        print("cód 4 rodando")
    elif op == 5:
        break
    else:
        print("digite uma opção valida")
print("ok! programa encerrado")

a = 2
b = 4
c = 8
d = 0
if ((a>=2) or (b<=3)):
    d = (a + c)/2;
else:
    d = b * c
print(d)

numero = 0
resultado = 0
while numero <= 10:
 resultado = 2 * numero
 print(f'2x {numero} = {resultado}')
 numero = numero + 1

resultado = 2 + 5 / 2
final = resultado - (resultado * (10/100))
print(resultado)
print(final)
if final <= 1:
    print("N1")
elif final <= 2:
    print("N2")
elif final <= 3:
    print("N3")
elif final <= 4:
    print("N1")
elif final <= 5:
    print("N5")

contador = 0
while (contador<=5):
    print(contador)
    contador = contador + 1

lista = [0,5,10,15,5,10,20]
print(lista.count(5))
'''
for numero in range (21):
    print(numero, end = " ")