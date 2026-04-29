# Entrada das notas
cp1 = float(input("Digite a nota do CP1: "))
cp2 = float(input("Digite a nota do CP2: "))
cp3 = float(input("Digite a nota do CP3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

# Descobrindo a menor nota dos checkpoints (sem usar min)
menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

# Soma dos 2 maiores checkpoints
soma_cp = cp1 + cp2 + cp3 - menor

# Média sem peso
media = ((soma_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)

# Média com peso
media_peso = media * 0.4

# Saída
print(f"\nMédia do semestre: {media:.1f}")
print(f"Média com peso: {media_peso:.1f}")
