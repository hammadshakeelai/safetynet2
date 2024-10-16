b=0
a=0
x=[1,7,6,4,7,9,18,3,5,1,7]
n=0
for i in range(x[2]):
    n=0
    while i != 0:
        if i<=0:
            break
        i-=1
        n+=1
    if a<=n:
        a=n
        if b<=n:
            b=a
print(a+b)