print("Welcome to logic QUIZ\n")
score=0
answer_dict={   0:{'question':'who is the best teacher?','options':"option 1. Fakhare Alam\noption 2.Shazad Khan\noption 3. Bahar Ali\noption 4. ALI haider\n",'answer':"4"},
                1:{"question":'what is my age?','options':"option 1. 41\noption 2. 93\noption 3. 27\noption 4. 1666\n",'answer':"4"},
                2:{"question":'what is my profession?','options':"option 1. terrorist\noption 2. CIA\noption 3. Doctor\noption 4. Doremon\n",'answer':"4"},
                3:{'question':'what is the current chinese year?','options':"option 1. dog\noption 2. elephant\noption 3. rabbit\noption 4. dragon\n",'answer':'4'},
                4:{'question':'how good is this program?','options':"option 1. A1\noption 2. BESTEST IN THE WORLD\noption 3. AAA\noption 4. islamabad good\n","answer":"4"}}
for i in range(5):
    print(f"\nQuestion {i+1}: {answer_dict[i]['question']}")
    print(answer_dict[i]['options'])
    answer=input("Enter Answer Number: ")
    if answer_dict[i]['answer']==answer: 
        print("correct")
        score+=1
    else: print("incorrect")
print("you has scored: ",score,"marks out of 5")