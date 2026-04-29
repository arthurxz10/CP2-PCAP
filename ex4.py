#Você foi contratado para criar um sistema de RH que calcula o
# salário final de um funcionário com base em
# diversos fatores: cargo, horas extras, faltas, bônus e descontos.

# Sistema de RH - Cálculo de Salário

def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas

def calcular_desconto_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "n":
        return 0

    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    else:
        return 100

# Entrada de dados
nome = input("Nome do funcionário: ")

print("Cargos: 1-Gerente  2-Analista  3-Assistente  4-Estagiário")
cargo = int(input("Cargo: "))

salario_base  = float(input("Salário base: "))
horas_extras  = int(input("Horas extras: "))
faltas        = int(input("Faltas no mês: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ").lower()

# Cálculos
extras    = calcular_horas_extras(salario_base, horas_extras)
bonus     = calcular_bonus(cargo, recebeu_bonus)
desconto  = calcular_desconto_faltas(salario_base, faltas)

total_acrescimos = extras + bonus
salario_bruto    = salario_base + total_acrescimos
salario_final    = salario_bruto - desconto

# Resultado
print("\n===== RESULTADO =====")
print(f"Funcionário:       {nome}")
print(f"Salário base:      R$ {salario_base:.2f}")
print(f"Total acréscimos:  R$ {total_acrescimos:.2f}")
print(f"Total descontos:   R$ {desconto:.2f}")
print(f"Salário bruto:     R$ {salario_bruto:.2f}")
print(f"Salário final:     R$ {salario_final:.2f}")
