
def funcaosemparametros():
    print("Olá")

def soma(num1, num2):
    return num1 + num2

def somaSubtracao(num1, num2):
    return num1 + num2, num1 - num2

def divisao(num1, num2=1):
    return num1 / num2

if __name__ == "__main__":
    funcaosemparametros()
    s = soma(5, 6)
    print(s)
    s1, sub1 = somaSubtracao(5, 9)
    d1 = divisao(10, 5)
    d2 = divisao(8)
    print(s, s1, sub1, d1, d2)