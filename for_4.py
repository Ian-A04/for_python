valor_final=int(input("Insira o valor final da sequência: "))

print("Sequência dos números: ")

ct=0

for x in range(valor_final + 1):
    print(x)
    ct=ct+1

print(f"A quantidade de números é de: {ct}")