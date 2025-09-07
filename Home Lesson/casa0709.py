# Exercício 1

nome = input ("Digite seu nome: ")
print("Boas-Vindas: " + nome)

# Exercício 2
var1 = int(input("Digite o primeiro num: "))
var2 = int(input("Digite o segundo numero: "))
print(var1 + var2)
print(var1 / var2)
print(var1 - var2)
print(var1 * var2)

# Exercício 3
var1 = int(input("Digite o primeiro num: "))
if    var1 % 2 == 0:
        print(var1,"é par")
else:
        print(var1,"é impar")

# Exercício 4
var1 = 1
while var1 <= 10:
    print("número ", var1)
    var1 = var1 + 1 

# Exercício 5
var1 = int(input("Digite o num: "))
contador = 1
while contador <= 10:
    var1 * contador
    print(var1 * contador)
    contador += 1


# Exercício 5

var1 = int(input("Digite a nota do primeiro semestre: "))
var2 = int(input("Digite a nota do segundo semestre: "))
var3 = int(input("Digite a nota do terceiro semestre: "))

media = (var1 + var2 + var3) / 3
print (media)

if media >= 7:
    print("Voçê foi aprovado")
else:
    print("Voçê foi reprovado")


# Exercício 6

var1 = int(input("Digite a nota do primeiro semestre: "))
var2 = int(input("Digite a nota do segundo semestre: "))
var3 = int(input("Digite a nota do terceiro semestre: "))

print("A maior nota é: " + str(max(var1,var2,var3)))