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
display_menu()