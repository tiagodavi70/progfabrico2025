
class Item():
    def __init__(self, nome, preco, tipo, imposto=0.23):
        self.nome = nome
        self.preco = preco
        self.imposto = imposto
        self.tipo = tipo
        
    def calcularPrecoComImposto(self):
        return self.preco + self.preco * self.imposto
    
    def __str__(self):
        return f"{self.nome} - {self.preco} - {self.tipo} - {self.imposto}"

if __name__ == "__main__":
    print("Olá")
    item1 = Item("aaa", 1, "bbb")
    item2 = Item("ccc", 1, "ddd", 0.2)

    print(item1, item2)
    item1.nome = "eee"
    print(item1.nome, item1.preco, item1.imposto, item1.tipo)
    print(item1.calcularPrecoComImposto())