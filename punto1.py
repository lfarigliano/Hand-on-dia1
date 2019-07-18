#Generador de numeros de 1 1000
a=range(3,1000,3)
c=range(5,1000,5)
resultList= set(a) | set(c)

d=sum(resultList)    
print (d)
    #resultado 233168
