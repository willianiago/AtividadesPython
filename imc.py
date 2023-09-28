#Olá, essa atividade é sobre IMC atividade realizada em 25/09/2023 às 22:23

print("Olá, seja bem vindo ao 'Meça aqui seu IMC grátis, rápido e fácil sem vírus'")
print("----------------------------------------------------------------------------")

#importando a biblioteca Matemática
import math

#obtendo dados dos usuários:

#cliente fornecendo a altura:
altura = float(input('Qual é sua altura? (m) '))
print("----------------------------------------------------------------------------")
#cliente fornecendo seu peso:
peso = float(input('Qual o seu peso? (Kg) '))
print("----------------------------------------------------------------------------")
#calculando o IMC
imc = peso / (altura ** 2)
#resultado do IMC
print("O seu IMC é de {:.1f}".format(imc))

#resultado do IMC em categorias
if imc < 18.5:
    print("Você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print("PARABÉNS voçê está no peso ideal")
elif 25 <= imc < 30:
    print("você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Cuidado, voçê está com OBESIDADE")
elif imc >= 40:
    print("Cara!! corre no médico, tu vai morrer")
print("----------------------------------------------------------------------------")

#conversa com o usuário
resposta = input("você gostou da experiência??[s/n]")
if (resposta == "s"):
    print("Muito Obrigado!!!")
else:
    print("poxa, vou melhorar para a próxima!!!")