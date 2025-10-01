# Escreva um script que receba um número no format CDU e converta
# para UDC (ex. 321 vira 123).

numeroCDU = input("Entra como o numero: ")
numeroCDU = int(numeroCDU)

C = numeroCDU // 100
D = (numeroCDU // 10) - (C * 10) ## 321 32
U = numeroCDU - ((C * 100) + (D * 10))

print(C, D, U)

numeroUDC = U * 100 + D *10 + C

print(numeroUDC)

