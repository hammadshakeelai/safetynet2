# find prime number
my_prime_list=[]
for i in range(12):
    if i==1 or i==0:
        continue
    prime=True
    for j in range(i-1):
        if j==1 or j==0:
            continue
        if i%j==0:
            prime=False
            break
    if prime:
        my_prime_list.append(i)
print(my_prime_list)
#two factor numbers
my_2facto_nums=[]
size=len(my_prime_list)
for i in range(size):
    if i==(size-1):
        continue
    for j in range(i+1,size):
        my_2facto_nums.append(my_prime_list[i]*my_prime_list[j])
print(my_2facto_nums)