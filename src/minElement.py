def fun(a):
    max=0
    najelement= a[0]
    for element in a:
        suma=0
        t=abs(element)
        while t!=0:
            c=t%10
            suma=suma+c 
            t=t//10
        if suma>max:
            max=suma
            najelement= element
        return najelement
        
a=[]
while 1:
    n=int(input())
    if n==0:
       break
    a.append(n)
print(fun(a))
