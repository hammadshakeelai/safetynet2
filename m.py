b=0
a=0
x=[1,7,6,4,7,9,2,3,5,110]
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
print(a+b)