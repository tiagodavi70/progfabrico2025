
class Contacto():
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def busca(self, termo):
        #return 1 <= len([1 for campo in [self.nome, self.telefone, self.email] if termo in campo])
        #campos = [self.nome, self.telefone, self.email]
        return termo in [self.nome, self.telefone, self.email]

    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.email}"

if __name__ == "__main__":
    contacto = Contacto("Tiago", "000000", "tiagodavi70@ua.pt")
    print(contacto)