db: dict[int,str]={
            0:"aleana",
            1:"nisha",
            2:"manoor",
            3:"maryam"
                   }
selection: int = 4   # selection = 4
if user := db.get(selection,'invalid'):
    print(f'You selected: {user}')
else:
    print(f'Invalid ID {selection}: No user found...')