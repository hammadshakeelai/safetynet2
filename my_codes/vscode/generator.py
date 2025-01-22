from typing import Generator
def func(n):
    mylist=[x for x in range(n+1)]
    for i in mylist:
        yield i
        
num =func(9)
print(next(num))
print(next(num))
print(next(num))
print(list(num))