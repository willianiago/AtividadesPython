produtos = []
estoque = []
preço = []
concluir = False

while (not concluir):
    print("Digite o nome do produto:")
    nomeProduto = input()
    print("Digite o estoque do produto")
    estoqueProduto = float(input())
    if(estoqueProduto < 15): print("bora estocar né?")
    elif(estoqueProduto < 10): print("fique ligado para não acabar logo")
    else: print("booooaa")
    print("Digite o preço do produto")
    preçoProduto = float(input())

    produtos.append(nomeProduto)
    estoque.append(estoqueProduto)
    preço.append(preçoProduto)
    


    print("Deseja inserir outra informação?(s/n)")
    concluir = input() == "n"

print(f"Seguem abaixo todas as informações digitadas:")
print(f"produto : estoque do produto : preço do produto")
for i in range(len(produtos)):
    print(f"{produtos[i]} : {estoque[i]} : R${preço[i]}")

input("Pressione Enter pra terminar...")
import os
filename = "meuArquivo.txt"
file = open(filename, "w")
for i in range(len(produtos)):
    outputline = f"NOME DO PRODUTO: {produtos[i]}\n QUANTIDADE NO ESTOQUE: {estoque[i]} \n PRECO: R${preço[i]}\n"
    file.write(outputline)
file.close()
os.system(f"notepad {filename}")