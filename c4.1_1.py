# Criar lista:
nome = ["thiago", "thiago", "Bruna", "Heloisa", "Gustavo"]
# Exibir a lista:
print(nome)
"""""
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

# Remover uma entrada (últim)
nome.pop(0)
for x in nome:
    print(x)

# Para remover um valor específico da lista:
nome.remove("Heloisa")
print(nome)
"""""
# Contar quantos itens há na lista:
print("O nome thiago aparece {}x".format(nome.count("thiago")))
# Contar o número de vezes que a string aparece na lista
contagem = nome.count("Heloisa")
print(contagem)
# Colocar a lista na ordem contrária
nome.reverse()
print(nome)
# Organizar em ordem alfabética
nome.sort()
print(nome)
# informar o tamanho do objeto
print(len(nome))

# Criar nova lista de elementos inteiros:
valores = [1, 2, 3, 5]
print(sum(valores))