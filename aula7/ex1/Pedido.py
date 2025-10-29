import datetime
from Item import Item


class Pedido():
    def __init__(self, itens, data=datetime.date.today):
        self.itens = itens
        self.data = data
        self.__id = None # atributo privado
    
    def valorTotal(self):
        if type(self.itens) == list:
            
            # soma = 0
            # for i in range(len(self.itens)):
            #     soma += self.itens[i].calcularPrecoComImposto()

            return sum(item.calcularPrecoComImposto() for item in self.itens)
        else:
            raise TypeError()
    
if __name__ == "__main__":
    item1 = Item("aaa", 1, "bbb")
    item2 = Item("ccc", 1, "ddd", 0.2)

    pedido1 = Pedido([item1, item2])
    print(pedido1.valorTotal())
    pedido2 = Pedido(item1)
    pedido2.valorTotal()