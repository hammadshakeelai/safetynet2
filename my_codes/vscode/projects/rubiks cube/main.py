yellow11 = yellow12 = yellow13 = yellow14 = yellow15 = yellow16 = yellow17 = yellow18 = yellow19 = 'y'
white31 = white32 = white33 = white34 = white35 = white36 = white37 = white38 = white39 = 'w'
green21 = green22 = green23 = green24 = green25 = green26 = green27 = green28 = green29 = 'g'
blue51 = blue52 = blue53 = blue54 = blue55 = blue56 = blue57 = blue58 = blue59 = 'b'
orange41 = orange42 = orange43 = orange44 = orange45 = orange46 = orange47 = orange48 = orange49 = 'o'
red61 = red62 = red63 = red64 = red65 = red66 = red67 = red68 = red69 = 'r'
def printcubex():
    print("         ", yellow11, yellow12, yellow13)
    print("         ", yellow14, yellow15, yellow16)
    print("         ", yellow17, yellow18, yellow19)
    print("         _______")
    print()
    print(green21, green22, green23, " | ", white31, white32, white33, " | ", blue51, blue52, blue53, " | ", red61, red62, red63)
    print(green24, green25, green26, " | ", white34, white35, white36, " | ", blue54, blue55, blue56, " | ", red64, red65, red66)
    print(green27, green28, green29, " | ", white37, white38, white39, " | ", blue57, blue58, blue59, " | ", red67, red68, red69)
    print("         _______")
    print()
    print("         ", orange41, orange42, orange43)
    print("         ", orange44, orange45, orange46)
    print("         ", orange47, orange48, orange49)
# printcubex()
def W_anticlock():
    white31,white39,white37,white33= white37,white33,white39,white31
    white36,white32,white34,white38= white38,white34,white32,white36
    orange41,orange42,orange43 = green23,green26,green29
    green23,green26,green29= yellow19,yellow18,yellow17
    yellow19,yellow18,yellow17= blue57,blue54,blue51
    blue57,blue54,blue51= orange41,orange42,orange43
W_anticlock()
printcubex()
