cp1 = float(input("CP1: "))
cp2 = float(input("CP2: "))
cp3 = float(input("CP3: "))
sp1 = float(input("Sprint 1: "))
sp2 = float(input("Sprint 2: "))
gs = float(input("Global Solution: "))

# achar a menor nota dos checkpoints
menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

# soma dos dois maiores
soma_cp = cp1 + cp2 + cp3 - menor

media = ((soma_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)
media_peso = media * 0.4

print(f"\nMédia: {media:.1f}")
print(f"Média com peso: {media_peso:.1f}")

