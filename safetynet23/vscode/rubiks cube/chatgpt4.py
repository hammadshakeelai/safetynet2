# Define cube faces as lists
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

def W_anticlock():
    # Rotate the white face
    white[0], white[2], white[6], white[8] = white[6], white[0], white[8], white[2]
    white[1], white[3], white[5], white[7] = white[3], white[7], white[1], white[5]

    # Adjust surrounding faces
    orange_temp = orange[0:3]
    orange[0:3] = green[2:9:3][::-1]
    green[2:9:3] = yellow[6:9][::-1]
    yellow[6:9] = blue[0:9:3]
    blue[0:9:3] = orange_temp
def w_clock():
    W_anticlock()
    W_anticlock()
    W_anticlock()

# W_anticlock()
# w_clock()

printcubex()
