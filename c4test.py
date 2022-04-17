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
'''
numero = 0
resultado = 0
while numero <= 10
