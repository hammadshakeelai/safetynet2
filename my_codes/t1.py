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


