yellow = ['y'] * 9
white = ['w'] * 9
green = ['g'] * 9
blue = ['b'] * 9
orange = ['o'] * 9
red = ['r'] * 9

def printcubex():
    print("         ", yellow[0], yellow[1], yellow[2])
    print("         ", yellow[3], yellow[4], yellow[5])
    print("         ", yellow[6], yellow[7], yellow[8])
    print("         _______")
    print()
    print(green[0], green[1], green[2], " | ", white[0], white[1], white[2], " | ",
          blue[0], blue[1], blue[2], " | ", red[0], red[1], red[2])
    print(green[3], green[4], green[5], " | ", white[3], white[4], white[5], " | ",
          blue[3], blue[4], blue[5], " | ", red[3], red[4], red[5])
    print(green[6], green[7], green[8], " | ", white[6], white[7], white[8], " | ",
          blue[6], blue[7], blue[8], " | ", red[6], red[7], red[8])
    print("         _______")
    print()
    print("         ", orange[0], orange[1], orange[2])
    print("         ", orange[3], orange[4], orange[5])
    print("         ", orange[6], orange[7], orange[8])

def U_anticlock():
    yellow_temp = [yellow[0], yellow[1], yellow[2]]
    yellow[0:3] = white[0:9:3][::-1]
    white[0:9:3] = green[0:9:3][::-1]
    green[0:9:3] = blue[0:9:3][::-1]
    blue[0:9:3] = red[0:9:3][::-1]
    red[0:9:3] = yellow_temp

def U_clock():
    U_anticlock()
    U_anticlock()
    U_anticlock()

def D_anticlock():
    yellow_temp = [yellow[6], yellow[7], yellow[8]]
    yellow[6:9] = blue[6:9][::-1]
    blue[6:9] = green[6:9][::-1]
    green[6:9] = white[6:9][::-1]
    white[6:9] = red[6:9][::-1]
    red[6:9] = yellow_temp

def D_clock():
    D_anticlock()
    D_anticlock()
    D_anticlock()

def L_anticlock():
    temp = [white[0], white[5], white[8]]
    white[0], white[2], white[8] = white[2], white[8], white[0]
    white[1], white[3], white[7] = white[3], white[7], white[1]
    white[4], white[6] = white[6], white[4]
    
    temp2 = [blue[0], blue[3], blue[6]]
    blue[0], blue[2], blue[8] = blue[2], blue[8], blue[0]
    blue[1], blue[4], blue[7] = blue[4], blue[7], blue[1]
    blue[2], blue[5] = blue[5], blue[2]
    
    temp3 = [green[0], green[3], green[6]]
    green[0], green[2], green[8] = green[2], green[8], green[0]
    green[1], green[4], green[7] = green[4], green[7], green[1]
    green[2], green[5] = green[5], green[2]
    
    temp4 = [red[0], red[3], red[6]]
    red[0], red[2], red[8] = red[2], red[8], red[0]
    red[1], red[4], red[7] = red[4], red[7], red[1]
    red[2], red[5] = red[5], red[2]
    
    temp5 = [orange[0], orange[3], orange[6]]
    orange[0], orange[2], orange[8] = orange[2], orange[8], orange[0]
    orange[1], orange[4], orange[7] = orange[4], orange[7], orange[1]
    orange[2], orange[5] = orange[5], orange[2]

def L_clock():
    L_anticlock()
    L_anticlock()
    L_anticlock()

def R_anticlock():
    temp = [white[2], white[5], white[8]]
    white[0], white[2], white[8] = white[8], white[0], white[2]
    white[1], white[3], white[7] = white[7], white[1], white[3]
    white[4], white[6] = white[6], white[4]
    
    temp2 = [blue[2], blue[5], blue[8]]
    blue[0], blue[2], blue[8] = blue[8], blue[0], blue[2]
    blue[1], blue[4], blue[7] = blue[7], blue[1], blue[4]
    blue[5], blue[7] = blue[7], blue[5]
    
    temp3 = [green[2], green[5], green[8]]
    green[0], green[2], green[8] = green[8], green[0], green[2]
    green[1], green[4], green[7] = green[7], green[1], green[4]
    green[5], green[7] = green[7], green[5]
    
    temp4 = [red[2], red[5], red[8]]
    red[0], red[2], red[8] = red[8], red[0], red[2]
    red[1], red[4], red[7] = red[7], red[1], red[4]
    red[5], red[7] = red[7], red[5]
    
    temp5 = [orange[2], orange[5], orange[8]]
    orange[0], orange[2], orange[8] = orange[8], orange[0], orange[2]
    orange[1], orange[4], orange[7] = orange[7], orange[1], orange[4]
    orange[5], orange[7] = orange[7], orange[5]

def R_clock():
    R_anticlock()
    R_anticlock()
    R_anticlock()

def F_anticlock():
    # Front face rotation
    temp = [yellow[0], yellow[1], yellow[2]]
    yellow[0], yellow[2], yellow[8] = yellow[2], yellow[8], yellow[0]
    
    temp2 = [orange[0], orange[1], orange[2]]
    orange[0], orange[2], orange[6] = orange[2], orange[6], orange[0]
    
    temp3 = [green[0], green[1], green[2]]
    green[0], green[2], green[6] = green[2], green[6], green[0]
    
    temp4 = [white[0], white[1], white[2]]
    white[0], white[2], white[6] = white[2], white[6], white[0]
    
    temp5 = [blue[0], blue[1], blue[2]]
    blue[0], blue[2], blue[6] = blue[2], blue[6], blue[0]
    
    temp6 = [red[0], red[1], red[2]]
    red[0], red[2], red[6] = red[2], red[6], red[0]
    
    # Middle layer rotation
    yellow[3:9] = white[3:9][::-1]
    orange[3:7] = green[3:8][::-1]
    green[3:8] = blue[3:8][::-1]
    blue[3:8] = red[3:8][::-1]

def f_clock():
    F_anticlock()
    F_anticlock()
    F_anticlock()

# F_anticlock()
# f_clock()

printcubex()

def B_anticlock():
    # Back face rotation
    temp = [yellow[6], yellow[7], yellow[8]]
    yellow[6], yellow[8], yellow[2] = yellow[8], yellow[2], yellow[6]
    
    temp2 = [orange[6], orange[7], orange[8]]
    orange[6], orange[8], orange[2] = orange[8], orange[2], orange[6]
    
    temp3 = [green[6], green[7], green[8]]
    green[6], green[8], green[2] = green[8], green[2], green[6]
    
    temp4 = [white[6], white[7], white[8]]
    white[6], white[8], white[2] = white[8], white[2], white[6]
    
    temp5 = [blue[6], blue[7], blue[8]]
    blue[6], blue[8], blue[2] = blue[8], blue[2], blue[6]
    
    temp6 = [red[6], red[7], red[8]]
    red[6], red[8], red[2] = red[8], red[2], red[6]
    
    # Middle layer rotation
    yellow[3:9] = white[3:9][::-1]
    orange[3:7] = green[3:8][::-1]
    green[3:8] = blue[3:8][::-1]
    blue[3:8] = red[3:8][::-1]

def b_clock():
    B_anticlock()
    B_anticlock()
    B_anticlock()

# B_anticlock()
# b_clock()
