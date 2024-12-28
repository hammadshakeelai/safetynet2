# Printing little fancy
campuses = ['Peshawar Campus', 'Islamabad Campus', 
            'Lahore Campus', 'Karachi Campus']
rooms = ['Room-1', 'Room-2', 'Room-3', 'Room-4', 'Room-5']

for campus in campuses:
    print("\n", campus, ":", sep="")
    for room in rooms:
        print(room)