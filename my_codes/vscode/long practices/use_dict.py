def logicquiz2():
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
def restaurantgpt():
    # Restaurant Menu and Ordering System

    # Menu stored as a dictionary
    menu = {
        "Pizza": 45678.9345679,
        "Burger": 5.49,
        "Pasta": 7.99,
        "Salad": 4.99,
        "Soda": 1.99,
        'ice cube': 0.01
    }

    def display_menu():
        print("Menu:")
        for item, price in menu.items():
            print(f"{item}: ${price:,.2f}")

    def take_order():
        order = {}
        while True:
            item = input("Enter the name of the item to order (or 'done' to finish): ").capitalize()
            if item == "Done":
                break
            elif item in menu:
                quantity = int(input(f"Enter quantity for {item}: "))
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
            else:
                print("Item not found on the menu. Please try again.")
        return order

    def generate_receipt(order):
        print("\nReceipt:")
        total = 0
        for item, quantity in order.items():
            price = menu[item] * quantity
            print(f"{item} x {quantity} = ${price:.2f}")
            total += price
        print(f"\nTotal: ${total:.2f}")

    # Main program
    print("Welcome to the Restaurant!")
    display_menu()
    order = take_order()
    if order:
        generate_receipt(order)
    else:
        print("No items ordered. Thank you!")
def logicquiz4():
    print("Welcome to logic QUIZ\n")
    score=0
    answer_dict={   0:{'question':'who is the best teacher?','options':"option 1. Fakhare Alam\noption 2.Shazad Khan\noption 3. Bahar Ali\noption 4. ALI haider\n",'answer':"4"},
                    1:{"question":'what is my age?','options':"option 1. 41\noption 2. 93\noption 3. 27\noption 4. 1666\n",'answer':"4"},
                    2:{"question":'what is my profession?','options':"option 1. terrorist\noption 2. CIA\noption 3. Doctor\noption 4. Doremon\n",'answer':"4"},
                    3:{'question':'what is the current chinese year?','options':"option 1. dog\noption 2. elephant\noption 3. rabbit\noption 4. dragon\n",'answer':'4'},
                    4:{'question':'how good is this program?','options':"option 1. A1\noption 2. BESTEST IN THE WORLD\noption 3. AAA\noption 4. islamabad good\n","answer":"4"}}
    for i in range(len(answer_dict)):
        print(f"\nQuestion {i+1}: {answer_dict[i]['question']}")
        print("Question: ", i+1 , answer_dict[i])
        print(answer_dict[i]['options'])
        answer=input("Enter Answer Number: ")
        if answer_dict[i]['answer']==answer: 
            print("correct")
            score+=1
        else: print("incorrect")
    print("you has scored: ",score,"marks out of 5")
def restaurant_practice_template():
    menu={
        0:{'name':"Chicken Fried Rice",'price':200},
        1:{'name':"Pad Thai",'price':1200},
        2:{'name':"Grilled Salmon",'price':2000},
        3:{'name':"Spring Rolls",'price':800},
        4:{'name':"Grilled Chicken Sandwich",'price':250},
        5:{'name':"Vegetable Curry",'price':450},
        6:{'name':"Thai Soup",'price':600},
        7:{'name':"Chocolate Lava Cake",'price':900},
        8:{'name':"Spaghetti Bolognese",'price':500}, 
    }
    def display_menu():
        print("MENU:")
        for i in range(len(menu)):
            print(menu[i]['name']+': ',menu[i]['price'])
    def take_order():
        pass
    def generate_receipt(order):
        pass
    # Main program
    print(menu)
    display_menu()
def restaurant2():
    # print(input("Error Restaurant.\nPress enter to show Menu"))
    total=0
    my_order_list = {}
    restaurant = {
        0:{'name':"Chicken Fried Rice",'price':200},
        1:{'name':"Pad Thai",'price':1200},
        2:{'name':"Grilled Salmon",'price':2000},
        3:{'name':"Spring Rolls",'price':800},
        4:{'name':"Grilled Chicken Sandwich",'price':250},
        5:{'name':"Vegetable Curry",'price':450},
        6:{'name':"Thai Soup",'price':600},
        7:{'name':"Chocolate Lava Cake",'price':900},
        8:{'name':"Spaghetti Bolognese",'price':500}, 
    }
    def show_menu():
        for i in range(len(restaurant)):
            print(f'option #{i+1}:{restaurant[i]['name']}---{restaurant[i]['price']}$\n')
    show_menu()
    while True:
        order =  int(input("What Would You Like to Order Sir:  "))
        correct_options=[1,2,3,4,5,6,7,8,9]
        while order not in correct_options:
            print("you have selected a wrong option")
            order =  int(input("What Would You Like to Order Sir:  "))
        servings = int(input("How Many servings of It Would You Like to Order"))
        while servings <0:
            print("you have selected a wrong option")
            servings = int(input("How Many servings of It Would You Like to Order: "))
        my_order_list[order] = servings
        for i,j in my_order_list.items():
            total += my_order_list[i]*restaurant[j]['price']
        break_statement=input("would you like to order More: press y : ")
        if break_statement.lower()!='y':
            break
    print(f' Your total is {total}')
    for i in my_order_list:
        print(restaurant[i-1]['name'])

