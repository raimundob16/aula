nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite uma nota: "))
media=(nota1+nota2)/2
print(media)
if media >= 9.0 and media < 10:
    
    print("Nota: A")
if media >=7.5  and media < 9.0:
    
    print("Nota: B")
if media >=6.0  and media < 7.5:
    
    print("Nota: C")
if media >=4  and media < 6.0:
    print("Nota: D")
if media <=4.0  and media > 0:
    print("Nota: E")
