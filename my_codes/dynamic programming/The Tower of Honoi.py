# def minimum_moves(number_of_discs: int)->int:
#     return (2**number_of_discs)-1

def minimum_moves(number_of_discs: int):
    if number_of_discs <= 1:
        return number_of_discs
    else:
        return minimum_moves(number_of_discs-1)*2+1
print(minimum_moves(9999))