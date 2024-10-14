x=int(input("enter the number you want to start the sequance from :  "))
n=int(input("enter number of iterations you want :  "))
print(x)# answer 1
fibonacci=x
print(fibonacci)# answer 1
g=fibonacci+fibonacci#g is the alternate storage for fibonacci
print(g)# answer 2
m=n-3
if m%2==0:
    n=m//2
else:
    m=m+1
    n=m//2
for i in range(n) :#while True:
    fibonacci=fibonacci+g
    print(fibonacci)#answer 3
    g=fibonacci+g
    print(g)#answer 5
#iam goated 