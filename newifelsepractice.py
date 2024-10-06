age=int(input("please enter your age here : "))
if age < 0 :
    print("age cannot be negetive")
elif age < 2:
    print("your person is a baby")
elif age < 8:
   print("your person is a young toddler")
elif age < 12:
    print("your person is a toddler ")
elif age < 19:
   print("your person is a teenager")
elif age < 24:
    print("your person is a minor")
elif age < 59:
   print("your person is a adult")
elif age < 85:
    print("your person is a senior citizen")
elif age > 85:
   print("your person is a dead body")
else :
   print("your person is buried under ground, rip.\n   sorry for you're loss.")