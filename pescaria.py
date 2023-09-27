kilos = float (input("digite a quantidade de pescado em KG: "))
  
if kilos > 50:
    multa = (kilos - 50)*4
    print ("Valor da multa é R$: ",multa)
else:
    print("Quantidade Liberada sem Multas")
