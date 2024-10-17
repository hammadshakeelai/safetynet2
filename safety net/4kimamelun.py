b=0
a=0
x=[1,1,1,7,4,0,100,44,3,100,44]#list of varring numbers
for i in list(x):#looping ever
    n=0
    while i != 0:
        if i<=0:
            break
        i-=1
        n+=1  
    if a<n and b!=n:
        a=n
    if b<a:    
        b,a=a,b
print(a+b)