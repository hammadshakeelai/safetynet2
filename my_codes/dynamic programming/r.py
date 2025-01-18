def combination(n,r):#formula?
    if n==r:
        return 1
    elif r==1:
        return n
    else: 
        return combination(n-1,r-1) + combination(n-1,r)
print(combination(5,))
# combination (n!)/(r!(n-r)!)#freedom of pickability
# permutation (n!)/((n-r)!)#freedom of pickability x possiblity of arrangements 

# (n)(c)(r)= (n-1)(c)(r-1) + (n-1)(c)(r)