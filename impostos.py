a = int (input("Quanto você ganha por hora: "))
b = int (input("digite quantas horas você trabalho: "))
salario = a*b
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario -ir-inss-sindicato
print ("O valor do INSS é R$:",inss)
print ("O valor do IMPOSTO DE RENDA é R$:",ir)
print ("O valor do SINDICATO é R$:",sindicato)
print ("O valor do SALARIO LIQUIDO é R$:",salario_liquido)