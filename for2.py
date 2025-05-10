fi=int(input("Digite o valor inicial da sequência: "))
ff=int(input("Digite o valor final da sequência: "))

print("Fahrenheit | Celsius")
print("-----------|---------")

if fi<ff:
    for f in range(fi,ff+1):
        c= 5*(f-32)/9
        print(f"     {f} ºF | {c:.3f} ºC ")

else:
    for f in range(fi,ff-1,-1):
        c = 5 * (f - 32) / 9
        print(f"      {f} ºF | {c:.3f} ºC ")