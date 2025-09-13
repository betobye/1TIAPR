preco = float(input("Entre com o preco do produto "))
quantidade = float(input("Entre com o quantidade adquirida "))
total = preco * quantidade
print(total)
if quantidade > 10:
    total = total * 0.9
print("Total a pagar : ", total)


idade = float(input("Entre com sua idade "))
if idade >= 16: 
    #--------------------------
    print("Voce pode voltar")
else:
    print("Voce não vai voltar")
    print("")
