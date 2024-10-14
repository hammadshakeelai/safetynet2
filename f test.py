y=1
n=10-3
x=1
print(y)
print(x)
z=x+y
print(z)
for i in range(n):
  y=x+z
  print(y)
  x,z=z,y   #x,z purane integers =  z,y naye integers
