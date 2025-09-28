primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))    
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = primeiro_numero + segundo_numero
elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
elif operacao == "/":
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

print("O resultado é:", resultado)      