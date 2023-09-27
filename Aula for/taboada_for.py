a = input("digite o uma operação: ")
b = int (input("digite um numero: "))

if a == '+':
    for i in range(1,11,):
        print("resultado de", i ,"+" ,b ,"=", i+b)
if a == '-':
    for i in range(1,11,):
        print("resultado de", i ,"-" ,b ,"=", i-b)
if a == '*':
    for i in range(1,11,):
        print("resultado de", i ,"*" ,b ,"=", i*b)
if a == '/':
    for i in range(1,11,):
        print("resultado de", i ,"/" ,b ,"=", i/b)