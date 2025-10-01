#Escreva um script que receba o valor do salário de um funcionário
# e o valor do salário mínimo. Calcule e mostre quantos
# salários mínimos ganha esse funcionário.

# 0 1 2
# 1 2 3
vetor = [1,2,3]

i = 1
print(vetor[i])

j = 1.0
#print(vetor[j])

salarioFuncionario = input("Entra com o salario do funcionário: ")
salarioFuncionario = float(salarioFuncionario)

salarioMinimo = input("Entra com o salário mínimo: ")
salarioMinimo = float(salarioMinimo)

print("O funcionario ganha", salarioFuncionario / salarioMinimo,
int((salarioFuncionario / salarioMinimo) + 0.5))
