a=[]
x = 1
suma=0
sum_int=0
a.append(x)
y = 1
a.append(y)
i = 1
sum_imp=2
while i <= 10000:
    i=i+1
    d=x+y
    suma=suma+d
    a.append(d)
    x=y
    y=d
    if d%2 !=0:
        if d < 1000000:
            sum_imp=sum_imp + d
print (sum_imp)
    #resultado 1089154

