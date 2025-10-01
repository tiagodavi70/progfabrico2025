# Sabe-se que o quilowatt de energia custa 2% do salário mínimo. Escreva um script que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência. Calcule e imprima:
#    o valor, em reais, de cada quilowatt;
#    o valor, em reais, a ser pago por essa residência;
#    o novo valor à ser pago por essa residência, se for dado um desconto de 15%


salarioMinimo = float(input("Entra com o salário minímo: "))

consumoQuilowatts = float(input("Entra com os quilowatts: "))

valorKw = salarioMinimo * (2/100)
consumo = valorKw * consumoQuilowatts

print(f"Valor do Kw: {valorKw}")
print(f"A residência paga: {consumo}")
print(f"Valor com desconto: {consumo - (consumo * (15/100))}")


