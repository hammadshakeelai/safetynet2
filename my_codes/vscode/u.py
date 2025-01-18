a=3
b=4
f=(lambda x,y: x+y)
print(f(a,b))
a=3
b=9
f= (lambda x,y:x+y)(a,b)
print(f)

print(f'Total Income: ${(lambda illegal_income,legal_income:illegal_income+legal_income)(9,9)}')
# map(lambda
# filter(lambda
# reduce(lambda
# yeild(lambda
mylist=[5,8,9,67]
print([2*x for x in mylist])