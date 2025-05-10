valor_inicial=int(input("Insira o valor inicial da sequência: "))

ct=0

print("Sequência de números:")

for x in range(valor_inicial,-1,-1):
    print(x)
    ct=ct+1

print(f"A quantidade de números é de: {ct}")