# Criar lista:
nome = ["thiago", "Bruna", "Heloisa", "Gustavo"]
# Exibir a lista:
print(nome)
# Exibir a lista por indice:
print(nome[1])
# Exibir item a item da lista usando loop for:
for x in nome:
    print(x)
# Inserindo um valor a nossa lista:
nome.append("Nicole")
print(nome)
# Para o usuário incluir um nome no fim da lista:
nome.append(input("Digite um nome"))
print(nome)
# Incluir o valor em uma posição especifica da lista:
nome.insert(2,"Jujuba")
print(nome)
# Usuário incluir valor que será colocado em um indice:
nome.insert(2,input("Coloque um novo valor para 2 "))
for x in nome:
    print(x)