# Exercícios

1. Implemente a classe `Felino`, e as subclasses `Gato`, `Tigre` e `Leão`. A classe Felino deve ter os atributos nome e peso, e um método que retorna se é doméstico ou não. Defina como deve ser o construtor de cada subclasse. Defina também usando polimorfismo se o Felino é ou não doméstico. Crie uma classe Zoologico com 40 animais para testar as classes criadas.

1. Utilizando a classe abaixo:
``` python
class Automovel:
    def __init__(self, modelo, litros_tanque, litros_km):
        self.modelo = modelo
        self.litros_tanque = litros_tanque  # litros que ainda estão no tanque
        self.litros_km = litros_km          # consumo de litros por km

    # Dado uma distância em km, calcula os litros utilizados
    def litros_utilizados(self, km: float) -> float:
        litros = km * self.litros_km
        self.consumir_tanque(litros)
        return litros

    # Consome a gasolina do tanque
    def consumir_tanque(self, litros):
        pass
```

termine a função consumirTanque e crie uma subclasse `Economico` que usa polimorfismo para diminuir o consumo em 3%. Crie 50 automóveis e corra 150km com cada um.

1. Crie duas classes: `Comodo` e `Casa`. Crie 10 casas com cómodos e apresente as informações sobre elas.
