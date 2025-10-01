
True
False

a = True
b = False

# c = a & b

operadorE = a and b # & && V
operadorOu = a or b # | || ^
operadorNao = not a # ~ ! 


idade = int(input("Entra com a tua idade: "))
residencia = input("Qual é o seu país de residência? ")
identificacao = bool(input("Tem identificação válida? "))

(identificacao) and ((idade >= 60) or (residencia == "Portugal"))

if ((idade >= 60) or (residencia == "Portugal")) and (identificacao):
    print("Tem direito a gratuidade")
else:
    print("Não tem direito a gratuidade")

entradaLogica = input("V ou F")

if entradaLogica == "V":
    entradaLogica = True
else:
    entradaLogica = False

entradaLogica = entradaLogica == "V"

if True:
    pass
else:
    if False:
        pass
    else:
        pass

if entradaLogica == "V":
    entradaLogica = True
elif entradaLogica == "F":
    entradaLogica = False
else:
    print("Não é um valor válido")

a = 1

cidade = "Oliveira de Azeméis"

match cidade:
    case "Porto":
        print("Porto")
    case "Oliveira de Azeméis":
        print("Oliveira de Azeméis!")
    case "Aveiro":
        print("Aveiro")

if cidade == "Porto":
    print("Porto")
elif cidade == "Oliveira de Azeméis":
    print("Oliveira de Azeméis")