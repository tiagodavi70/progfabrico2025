
class Forma():
    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):
        if lado <= 0:
            raise ArithmeticError("Lado negativo")
        else:
            self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado


def ProprioErro(Exception):
    def __init__(self, mensagem, valor):
        self.message = mensagem
        self.valor = valor

if __name__ == "__main__":

    try:
        quadrado = Quadrado(-5)
        print(quadrado.perimetro())
    except ArithmeticError as e:
        print("Não pode ter um lado negativo")
        print(f"Erro: {e.args[0]}")
