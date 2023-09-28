distancia = float(input("Digite a distancia"))
velocida = float(input("Digite a velocidade"))
temp_minutos = (distancia/velocida)

hora = int(temp_minutos)
minutos = int(temp_minutos - hora)*60
segundos = int(((temp_minutos - hora)*60-minutos)*60)
print(f"tempo estimado da viagem:{hora} horas, {minutos} minutos eé {segundos}")