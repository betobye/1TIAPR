valprod = input("Digite o valor do produto: ")
valprod = float(valprod)

if valprod > 100:
    valprod = valprod * 0.9
    print(f"O valor do produto com desconto é {valprod:.2f}")   