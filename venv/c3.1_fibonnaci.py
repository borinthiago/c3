'''
Nesse jogo o jogador deverá acertar se um número encontra-se na sequência de Fibonacci.
'''

print("Bem vindo ao gamequest de Fibonacci\n")
valor = int(input("Digite um valor da sequencia de Fibonacci: "))

anterior1 = 1
anterior2 = 0
for n_elemento in range(1, valor + 1,1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = int(atual)
    print(atual)
    if valor == atual:
        print("Ação bem sucedida.")
        break
    elif valor < atual:
        print("Ação mal sucedida")
        break



