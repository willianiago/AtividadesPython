import random
print()
print("Olá sejam bem vindos ao sorteio de nome!!!")
print("----------------------------------------------")

n1 = str(input("Digite o primeiro nome "))
n2 = str(input("Digite o segundo nome "))
n3 = str(input("digite o terceiro nome "))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print("a pessoa escolhida foi: {} ".format(escolhido))