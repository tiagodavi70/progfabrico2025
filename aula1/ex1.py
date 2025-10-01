# Escreva um script que receba três nomes e mostre na tela da ordem reversa da entrada.

nome1 = input("Entra com o primeiro nome: ")
nome2 = input("Entra com o segundo nome: ")
nome3 = input("Entra com o terceiro nome: ")

print(nome3, nome2, nome1)

vetorNomes = [nome1, nome2, nome3]
vetorNomes.append("Tiago")

vetorNomes[::-1]

for i in range(len(vetorNomes) - 1, -1, -1):
    print(vetorNomes[i])

for j in range(5, 15, 2):
    print(j)