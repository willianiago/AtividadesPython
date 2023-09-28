
nome = str(input('Digite o nome do contato '))
sobrenome = str(input('Digite o sobrenome do contato '))
numero = str(input('Digite agora o número do contato '))
a = input('deseja adicionar mais alguém? [s/n]')

if (a == "s"):
    nome = str(input('Digite o nome do contato '))
    sobrenome = str(input('Digite o sobrenome do contato '))
    numero = str(input('Digite agora o número do contato '))
elif (a == "n"):
    print("ficamos por aqui")


contato = [nome, sobrenome, numero]


