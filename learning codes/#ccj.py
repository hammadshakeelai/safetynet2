y=input("y ")
x=input("x")
z=int(x)+int(y)
print(z)

y=int(input("y "))
x=int(input("x "))
print(x+y)

print(int(input("y "))+int(input("x ")))

y=float(input("y "))
x=float(input("x "))
print(x+y)

print(round(x+y))
print(round(x+y,2))

y=float(input("y "))
x=float(input("x "))
z=round(x+y)
print(f"{z:,}")#to add , after 3 digits of number

print(f"{z:.2f}")#goes upto two decimal points 

def hh(to):
    print("hello,",to)
name=input("enterv nmae ?? ")
hh(name)