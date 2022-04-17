"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para
a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que
cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
obtiveram, verifique e exiba qual dia foi o escolhido.
"""
# Apresentar o programa:
print("\nVotação para definiçao do dia da semana em que ocorrerá o FIAP Live\n")

# Informar as variáveis:
alunos = int(input("Por favor digite a quantidade de alunos na turma: "))
i = 0
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
nulo = 0

# Criar laço para contabilizar os votos:
for x in range(0, alunos, 1):
    i = i + 1
    print("\nAluno {}\n\n1 para Segunda\n2 para terça\n3 para quarta\n4 para quinta\n5 para sexta".format(i))
    voto = int(input("\nSeu voto: "))
    if voto == 1:
        segunda = segunda + 1
    elif voto == 2:
        terca = terca + 1
    elif voto == 3:
        quarta = quarta + 1
    elif voto == 4:
        quinta = quinta + 1
    elif voto == 5:
        sexta = sexta + 1
    else:
        nulo = nulo + 1

print("\nO total de votos foi:\nSegunda-feira: {} votos\nTerça-feira: {} votos\nQuarta-feira: {} votos\n"
      "Quinta-feira: {} votos\nSexta-feira:{}\nNão computados: {} votos".format(segunda, terca, quarta, quinta, sexta, nulo))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\nO dia escolhido foi SEGUNDA-FEIRA")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\nO dia escolhido foi TERÇA-FEIRA.")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print('\nO dia escolhido foi QUARTA-FEIRA.')
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print('\nO dia escolhido foi QUINTA-FEIRA.')
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print('\nO dia escolhido foi SEXTA-FEIRA.')
else:
    print('Houve empate e será necessária nova votação.')