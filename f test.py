m=int(input("enter number of iterations :  "))
y=0
n=m-2 #ten is the amount of printed number of fibonacci sequnce
x=1

if n <=1:
  print(y)

if n<=2:
  print(x)

for i in range(n):
  z=x+y
  print(y)
  x,y=z,x  #x,z purane integers =  z,y naye integers
