A = [21, 9, 3, 9, 8, 7, 3, 9, 7, 9, 9, 7, 21, 9, 8]
list=[]
for i in A:
    list.append(i)

for i in range(len(A)):
    flag=True 
    for o in range(len(list)):
        a=o
        if o != i and A[a]==A[i]:
            A.remove(A[i])
            A.remove(A[i])
print(A[0])
    
    
    
    
    
    
    
    

A=list