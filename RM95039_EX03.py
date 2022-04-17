"""
3 – Muitos professores preferem adotar modelos diferentes de provas. Por essa razão, a escola de inglês
JoWell Sant’ana, em que as turmas são compostas por 50 alunos, solicitou que você criasse um sistema
capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que
têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par
(2, 4, 6..., 48, 50).

O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual
delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar
cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
"""

# Apresentar o programa:
print("\nBem vindo ao portal de notas da escola JoWell Sant’ana.")

# Declarar variáveis:
i = -1
p = 0
soma_impar = 0.0
soma_par = 0.0

# Criar loop for para inserção da nota do lado impar no sistema:
for n_impar in range(1, 50, 2):
    i = i + 2
    nota_impar = float(input("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    soma_impar = soma_impar + nota_impar

# Criar loop for para inserção da nota do lado par no sistema:
for n_par in range(2, 52, 2):
    p = p + 2
    nota_par = float(input("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(p)))
    soma_par = soma_par + nota_par

# Calcular as médias e armazenar para exibir:
media_impar = float(soma_impar) / 25
media_par = float(soma_par) / 25

# Exibir média armazenada:
print("\nA nota média da metade impar da sala é {}.".format(media_impar))
print("A nota média da metade par da sala é {}.".format(media_par))

# Comparar qual foi a maior média ou se houve empate:
if media_impar > media_par:
    print("\nA metade IMPAR teve maior nota.")
elif media_impar < media_par:
    print("\nA metade PAR teve maior nota.")
else:
    print("\nAs duas metades PAR e IMPAR tiverem médias iguais.")
input("\nPresione qualquer tecla para sair: ")