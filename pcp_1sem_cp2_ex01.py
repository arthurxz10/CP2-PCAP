#▪ Faça um programa que recebe:
#▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
#▪ o peso da carga do caminhão em toneladas
#▪ o código da carga, supondo que é um número inteiro de 10 e 40
#▪ Seu programa deve calcular:
#▪ o peso da carga do caminhão convertido em quilos
#▪ o preço da carga do caminhão
#▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
#▪ o valor total transportado pelo caminhão (carga + impostos)
codigo_estado = int(input("Digite o código do estado de origem (de 1 a 5): "))
peso = (float(input("Digite o peso em toneladas: ")))
codigo_carga = int(input("Digite o código da sua carga (de 10 a 40): "))
peso_convertido = peso * 1000
if 10 <= codigo_carga <= 20:
    preco_kg = 100.0
elif 21 <= codigo_carga <= 30:
    preco_kg = 250.0
elif 31 <= codigo_carga <= 40:
    preco_kg = 340.0
preco_carga = preco_kg * peso_convertido
match codigo_estado:
    case 1:
        imposto = 0.35
    case 2:
        imposto = 0.25
    case 3:
        imposto = 0.15
    case 4:
        imposto = 0.05
    case 5:
        imposto = 0.0
valor_imposto = preco_carga * imposto
valor_total = preco_carga + valor_imposto
print(f"Peso em Kg {peso_convertido: }")
print(f"Preço da carga R${preco_carga: }")
print(f"Valor do imposto R${valor_imposto: }")
print(f"Valor total R${valor_total: }")