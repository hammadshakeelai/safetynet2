def answer_checker(n):
    power=0
    k=0
    while n>k:
        k=pow(2,power)
        if k!=0:
            power+=1
    if n==k:
        p=n-k
    else:
        k/=2
        p=n-k
    p*=2
    p+=1
    return int(p)
