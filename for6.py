nmr=int(input("Digite o número base para a tabuada: "))

print(f"Tabuada do {nmr}")

for x in range(1,10+1):
    multiplicacao = nmr*x
    print(f" {nmr} x {x:2} = {multiplicacao}")