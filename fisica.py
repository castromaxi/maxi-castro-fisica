animalac=float(input("cuanta es la acerelacion del animal? "))
animalvf=float(input("cuanta es la velocidad maxima del animal? "))
corredorac=float(input("cuanta es la acerelacion del corredor? "))
corredorvf=float(input("cuanta es la velocidad maxima del corredor? "))
distancia=float(input("cuanta es la distancia entre los 2? "))
tiempoanimal=animalvf/animalac
tiempoanimal=round(tiempoanimal,2)
tiempocorredor=corredorvf/corredorac
tiempocorredor=round(tiempocorredor,2)
print ("el tiempo que le toma al animal llegar a su velocidad maxima es", tiempoanimal)
print ("el tiempo que le toma al corredor llegar a su velocidad maxima es", tiempocorredor)
metrosanimal=0.5*animalac*tiempoanimal**2
metrosanimal=round(metrosanimal,2)
metroscorredor=0.5*corredorac*tiempocorredor**2
metroscorredor=round(metroscorredor,2)
print ("los metros que le toma al animal llegar a su velocidad maxima es", metrosanimal)
print ("los metros que le toma al corredor llegar a su velocidad maxima es", metroscorredor)

## comentario