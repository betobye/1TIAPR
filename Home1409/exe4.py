lista_nomes = ["Ana", "Bia", "Carlos", "Daniel", "Rafaela"]
input_nome = input("Digite um nome: ")
if input_nome in lista_nomes:
    print(f"{input_nome} está na lista.")
else:
    print(f"{input_nome} não está na lista.")