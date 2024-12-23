dict={
            0:"aleana" ,
            1:"nisha" ,
            2:"manoor" ,
            3:"maryam"
}
selection= 3 
name=dict.get(selection)
if name:
    print(f'You selected: {name}')
else:
    print(f'Invalid ID {selection}: No user found...')