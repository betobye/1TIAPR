temperatura = int(input("Digite a temperatura em Celsius: "))
if temperatura < 0:
    print("Está congelante")
elif temperatura > 0 and temperatura < 30:
    print("Está agradável")
else:
    print("Está quente")
