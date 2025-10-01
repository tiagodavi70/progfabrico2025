# Um trem se locomove há 150 km/h, e funciona por 20 horas por dia.
# A cada 2.000 km ele deve parar 6 horas para manutenção.
# Cada manutenção custa R$ 2.000,00 e a cada 3 dias é
# cobrada uma taxa de R$ 5.000,00 de uso da ferrovia.
# Escreva em um script que receba o número de dias e
# escreva na tela um relatório, com o número de kilômetros
# percorridos e manutenções realizadas, assim como o custo total.

# 150 * 20

dias = int(input(" entra com o número de dias: "))
tempoTotal = dias * 20
distanciaTotal = tempoTotal * 150
numeroParadas = distanciaTotal // 2000

tempoTotal = tempoTotal - (6 * numeroParadas)

custoDias = 5000 * (dias // 3)
custoTotal = (numeroParadas * 2000) + custoDias

print(f"Km: {distanciaTotal}\nParadas {numeroParadas}\nCusto: {custoTotal}")
