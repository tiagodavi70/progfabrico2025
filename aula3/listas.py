
lista = []

lista.append(1)
lista.append(4)
lista.append(5)

print(lista)


lista_valorada = [1, 2, 3, 4, 5]

print(lista_valorada)

lista_preenchida = []

for i in range(10):

    lista_preenchida.append(i)
print(lista_preenchida)


lista_preenchida2 = list(range(10))

print(lista_preenchida2)


print(lista_preenchida[0])
print(lista_preenchida[2])

j = 8

print(lista_preenchida[j])
# print(lista_preenchida[10])
parte_lista = [] # 4-7

for i in range(4,8):
    parte_lista.append(lista_preenchida[i])
print(parte_lista)

parte_lista2 = lista_preenchida[4:8]
print(parte_lista2)

tamanho = len(lista_preenchida)
print(lista_preenchida[tamanho - 1])
print(lista_preenchida[-1])
print(lista_preenchida[-2])

nome_ficheiro = "texto.docx"

print(nome_ficheiro[-4:])

print(nome_ficheiro[:-4])

matriz = [[1,2], [3,4]]

print(matriz)
print(matriz[0][1])