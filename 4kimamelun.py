b=0
a=0
x=[1,1,1,1,1,1,1,3000,10,3000]
for i in list(x):
    n=0
    while i != 0:
        if i<=0:
            break
        i=i-1
        n=n+1  
    if a<=n:
        a=n
        if b<a and b!=a:
            b,a=a,b
print("misterrr beeeassstt",a+b, "ooooooOOooo")