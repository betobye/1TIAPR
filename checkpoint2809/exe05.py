firstnum = input("Digite o primeiro número: ")
firstnum = int(firstnum)

secondnum = input("Digite o segundo número: ")
secondnum = int(secondnum)

if firstnum == secondnum:
    print("Os números são iguais.")
elif firstnum > secondnum:
    print("O primeiro número é maior.")
else:
    print("O segundo número é maior .")