input_num_pri = input("Digite o primeiro número: ")
input_num_sec = input("Digite o segundo número: ")
input_num_ter = input("Digite o terceiro número: ")

soma = (int(input_num_pri) + int(input_num_sec) + int(input_num_ter))
print(soma)
elementos = (len([input_num_pri, input_num_sec, input_num_ter]))
print(elementos)
media = soma / elementos
print(media)