# pcp_1sem_cp2_ex05.py
# Sistema de financiamento com parcelas fixas (Tabela Price)
 
 
def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= 20 * renda:
        return True
    else:
        return False
 
 
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10
 
 
def calcular_parcela(valor, taxa, parcelas):
    fator = (1 + taxa) ** parcelas
    pmt = valor * (taxa * fator) / (fator - 1)
    return pmt
 
 
def calcular_total(parcela, parcelas):
    return parcela * parcelas
 
 
def calcular_juros(total, valor):
    return total - valor
 
 
# ------======---- programa principal ----------
nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal (R$): "))
valor = float(input("Valor desejado do empréstimo (R$): "))
parcelas = int(input("Número de parcelas (3 a 24): "))
 
if pode_aprovar(idade, renda, valor):
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)
 
    print("\n=== EMPRESTIMO APROVADO ===")
    print(f"Cliente............: {nome}")
    print(f"Valor financiado...: R$ {valor:.2f}")
    print(f"Taxa de juros......: {taxa * 100:.1f}% ao mês")
    print(f"Valor da parcela...: R$ {parcela:.2f}")
    print(f"Valor total pago...: R$ {total:.2f}")
    print(f"Total de juros.....: R$ {juros:.2f}")
else:
    print("\n=== EMPRESTIMO NEGADO ===")
    print(f"Cliente: {nome}")
    print("Motivo: idade insuficiente ou valor acima de 20x a renda mensal")