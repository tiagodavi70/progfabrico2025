# Escreva um script que receba um número
# indeterminado de valores,
# e conte os números entre 50 e 150.

contador = 0
numero = 0

while numero != -1:
    numero = input("Entra com um numero (entra com -1 se deseja parar): ")
    numero = int(numero)

    if (numero > 50) and (numero < 150):
        contador = contador + 1
    
    #deseja continuar?
print("Valores entre  50 e 150: ", contador)