#criando a variável RESPOSTA
resposta = int(input("which is the meaning of life? "))
i=int(0)

#criando a condição esperado, enquanto não for atingida o sistema repete

while resposta != 42 and i<2 :
        resposta = int(input("Try again: "))
        i = i+1
        #uma vez a condição esperada atingida o sistema emite a mensagem
        print("You are right {} is the meaning of life".format(resposta))
