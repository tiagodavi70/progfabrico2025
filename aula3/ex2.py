# Escreva um script que crie um vetor com 10 posições
# e receba seus valores do usuário. Ao final deverá
# mostrar somente os valores acima da média.

valores = [] # [0] * 10
for i in range(10):
    #valores[i] = int(input("Entra com o valor: "))
    valores.append(int(input("Entra com o valor: ")))

soma = 0
for i in range(10):
    soma += valores[i]
media = soma / len(valores)

for i in range(10):
    if valores[i] > media:
        print(valores[i])
