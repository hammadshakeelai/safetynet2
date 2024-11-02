name=input("nmae??/")
name=name.strip()#to remove spaces from string
name=name.capitalize()#to capitalize first alphabet
name=name.title()#to capatilize first letter of every word
print(f"hello, {name}")
name=name.capitalize().strip()
name=input("nmae??/").capitalize().strip()

first, last =name.split(" ")
print(first)