numero=[]
par=[]
imp=[]
for i in range(10):
    num = int(input("Digite um numero"))
    numero.append(num)
    
    if numero[i] % 2 == 0:
        par.append(numero[i])
    else: 
        imp.append(numero[i])
print("numeros",numero)
print("pares",par)
print("impar",imp)