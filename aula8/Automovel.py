class Automovel():
    def __init__(self, modelo, combustivel=50):
        self.modelo = modelo
        self.combustivel = combustivel
    
    def consumir(self, combustivel):
        self.combustivel = max([0, self.combustivel - combustivel])
        # if self.combustivel - combustivel > 0:
        #     self.combustivel = self.combustivel - combustivel
        # else:
        #     self.combustivel = 0
        # self.combustivel = self.combustivel - combustivel if self.combustivel - combustivel > 0 else 0
        
    def __str__(self):
        return f"{self.modelo} | {self.combustivel}"
    
class Bicicleta(Automovel):

    def __init__(self, modelo):
        self.modelo = modelo
        del self.combustivel

    def marchas(self, marchas):
        self.m = marchas
    
    # def consumir(self, combustivel):
    #     self.combustivel = 0

    def __str__(self):
        return f"{self.modelo}"

class AutoEco(Automovel):
    
    def consumir(self, combustivel):
        self.combustivel = super().consumir(combustivel) * .8 

if __name__ == "__main__":
    automovel1 = Automovel("AAA", 50)
    automovel2 = Bicicleta("BBB")

    print(automovel1.modelo, automovel2.modelo)
    automovel2.marchas(4)
    automovel2.consumir(0)
    print(automovel2.combustivel)
    # automovel1.marchas(4) # ERRO ERRO

    automovel3 = AutoEco("CCC")
    automovel3.consumir(20)
    print(automovel3.combustivel)

