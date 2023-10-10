produto1= float(input("Digite o Valoe do produto A: "))
produto2= float(input("Digite o Valoe do produto B: "))
produto3= float(input("Digite o Valoe do produto C: "))

if produto1 < produto2 and produto1< produto3:
    print("O produto A",produto1," é mais barato")
elif produto2 < produto1 and produto2 < produto3:
    print("O produto B",produto2," é mais barato")
else:
    print("O produto C",produto3," é mais barato")