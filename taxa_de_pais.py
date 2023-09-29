paisA = 80000
paisB = 200000
anos = 0
cresA =  0.03
cresB = 0.015 
while (paisA < paisB):
    anos += 1
    paisA = paisA + (paisA * cresA)
    paisB = paisB + (paisB * cresB)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
