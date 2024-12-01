def i_in_list(i,list):
    for j in range(len(list)):
        if list[j]==i:
            return True
    return False

list=[7,9,0,4,6,2]
print("True") if i_in_list(9,list) else print("False")