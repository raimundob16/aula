while True:
    nota = float(input("digite um numero entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        print("nota digitada ",nota)
        break
    else:
        print("nota invalida!")
