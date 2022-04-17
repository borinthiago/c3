"""
def calcularvelocidademedia():
    # Criar variáveis:
    distancia = float(input("Indique a percorrida (KM):  "))
    tempo = float(input("Indique o tempo da viagem (h):  "))
    # Fazer o calculo:
    velocidade = distancia // tempo
    # Exibir o calculo:
    print("A valocidade foi de {}KM/h".format(velocidade))

# Chamar a função:
calcularvelocidademedia()

# Aplicando as boas práticas:
distancia = float(input("Indique a percorrida (KM):  "))
tempo = float(input("Indique o tempo da viagem (h):  "))

def calcularvelocidademedia(distancia, tempo):
    # Fazer o calculo:
    velocidade = distancia // tempo
    # Exibir o calculo:
    print("A valocidade foi de {}KM/h".format(velocidade))

calcularvelocidademedia(distancia, tempo)
"""
# Função de cálculo de velocidade
def calcularvelocidademedia(distancia, tempo):
    # Fazer o calculo:
    velocidade = distancia // tempo
    # Exibir o calculo:
    return velocidade
# Entrada das variáveis:
distancia = float(input("Indique a percorrida (KM):  "))
tempo = float(input("Indique o tempo da viagem (h):  "))
# Chamada da função com os valores definidos pelo usuário:
print("A velocidade média foi de {}km/h".format(calcularvelocidademedia(distancia,tempo)))
