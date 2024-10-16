m=int(input("enter number of iterations :  "))
y=0
x=1
if m >=1:
  print("0")
if m>=2:
  print(x)
for i in range(2,m):
  z=x+y
  print(z)
  x,y=z,x  #x,z purane integers =  z,y naye integers