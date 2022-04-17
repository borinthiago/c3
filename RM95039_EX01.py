"""
1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver
um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para
gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um
sistema de assinaturas e um bônus calculado por uma porcentagem sobre o faturamento que o canal
do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele
e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra
a porcentagem de acordo com cada nível de assinatura:

Nível
Basic --------- 30%
Silver -------- 20%
Gold ---------- 10%
Platinum ------ 5%
"""

# Apresentar o programa ao usuário:
print("\nBem vindo ao Serviço de Streaming FIAP ON.\n")

# Solicitar o tipo de assinatura do usuário e o faturamento do usuário:
assinatura = str(input("Por favor, informe seu tipo de assinatura Basic, Silver, Gold ou Platinum:\nAssinatura: "))
faturamento = float(input("Por favor, informa quel é o faturamento anual do seu canal: \nFaturamento: "))

# Calcular o bônus baseado no tipo de assinatura do usuário e exibir valor a ser pago:
if assinatura.upper() == 'BASIC':
    bonus = faturamento * 0.3
    print("O cliente tem assinatura BASIC, portanto deverá pagar R${:.2f} de bônus.".format(bonus))
elif assinatura.upper() == 'SILVER':
    bonus = faturamento * 0.2
    print("O cliente tem assinatura SILVER, portanto deverá pagar R${:.2f} de bônus.".format(bonus))
elif assinatura.upper() == 'GOLD':
    bonus = faturamento * 0.1
    print("O cliente tem assinatura GOLD, portanto deverá pagar R${:.2f} de bônus.".format(bonus))
elif assinatura.upper() == 'PLATINUM':
    bonus = faturamento * 0.05
    print("O cliente tem assinatura PLATINUM, portanto deverá pagar R${:.2f} de bônus.".format(bonus))

# Gerar mensagem caso tipo de assinatura informada não exista:
else:
    print("Tipo de assinatura não válida, por favor verificar assinatura.")

input("\nPresione qualquer tecla para sair: ")
