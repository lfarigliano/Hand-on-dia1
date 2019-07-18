#n=600851475143
#a=list(range(1,n))    #600851475143
#primos=[]
#while len(a)>0:
#    primos.append(a[0])
#    a.remove(a[0])
#    test=primos[-1]
#    for i in a:
#        if i%test == 0:
#            a.remove(i)
##print (primos)            
#for i in primos:
#    if n%i==0:
#       print (i)   
# Lo de arriba no sirve porque creas una lista muy grande, y la memoria no anda
a=600851475143
b=2
while a>b:
    if a%b == 0:
        a=a/b
        b=2
    else:
        b=b+1
print (b)    
