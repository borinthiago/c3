from function import menu

user = ""
password = ""
i = 0
while (user != "admin" and password != "123"):
    print("\nFaça login")
    user = input("Digite o user: ")
    password = input("Digite o password: ")
    i = i + 1
else:
    print("Você esta logado, após {} tentativas.".format(i))
    menu()
