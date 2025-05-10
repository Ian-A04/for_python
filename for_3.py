print("Sequência dobro dos números de 1-10")

ct=0
soma=0

for x in range(0,21,2):
    print(x)
    soma = soma + x
    ct=ct+1

media= soma/ct

print(f"A soma dos números é de: {soma}")
print(f"A média dos números é de: {media}")