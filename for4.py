print("soma de todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três entre 1 a 500")

soma=0

for x in range(1,500+1):
    if x % 2 != 0 and x % 3 == 0:
        soma = soma + x

print(f"Soma dos números: {soma}")