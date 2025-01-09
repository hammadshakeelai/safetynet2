print("############")
print("Welcome to logic QUIZ")
print()
name=input("Enter Your Name:  ")
###############################################
score=0
print()
Q1="Question Number 1: who is the best teacher?\noption 1. Fakhare Alam\noption 2.Shazad Khan\noption 3. Bahar Ali\noption 4. ALI haider\n\nEnter Answer Number: "
Q2="Question Number 2: what is my age?\noption 1. 41\noption 2. 93\noption 3. 27\noption 4. 16\n\nEnter Answer Number: "
Q3="Question Number 3: what is my profession?\noption 1. terrorist\noption 2. CIA\noption 3. Doctor\noption 4. Doremon\n\nEnter Answer Number: "
Q4="Question Number 4: what is the current chinese year?\noption 1. dog\noption 2. elephant\noption 3. rabbit\noption 4. dragon\n\nEnter Answer Number: "
Q5="Question Number 5: how good is this program?\noption 1. A1\noption 2. BESTEST IN THE WORLD\noption 3. AAA\noption 4. islamabad good\n\nEnter Answer Number: "

answer_dict={
    Q1:1,
    Q2:3,
    Q3:2,
    Q4:1,
    Q5:2
}
print(Q1,end="")
answer=input("")
if answer_dict[Q1]==int(answer):
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print(Q2,end="")
answer=input("")
if answer_dict[Q2]==int(answer):
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print(Q3,end="")
answer=input("")
if answer_dict[Q3]==int(answer):
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print(Q4,end="")
answer=input("")
if answer_dict[Q4]==int(answer):
    print("Correct")
    score+=1
else:
    print("Incorrect")
print(Q5,end="")
answer=input("")
if answer_dict[Q5]==int(answer):
    print("Correct")
    score+=1
else:
    print("Incorrect")
print(name, "has scored: ",score,"marks out of 5")