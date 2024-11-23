def lists():
    # first_list = [1, 2, 3]
    # second_list = [1, 2, 3]

    # first_list = [1, 2, 3]
    # second_list = [3, 2, 1]

    # first_list = []
    # second_list = [1, 2, 3]

    # first_list = [1, 2, 3]
    # second_list = ['1', '2', '3']

    # first_list = [1, [2, 3], 4]
    # second_list = [1, [2, 3], 4]

    # first_list = ['Apple', 'banana']
    # second_list = ['apple', 'Banana']

    # first_list = [1, 2, 3]
    # second_list = [1, 3, 4]

    # first_list = ['A', 'B', 'C']
    # second_list = ['a', 'b', 'c']

    # first_list = [[1, 2], [3, 4]]
    # second_list = [[1, 2], [4, 3]]

    # first_list = [[], [1, 2, 3]]
    # second_list = [[], [1, 2]]

    # first_list = [1.0, 2.0, 3.0]
    # second_list = [1, 2, 3]

    # first_list = ['a', 2, [3, 'b']]
    # second_list = ['a', 2, [3, 'B']]

    first_list = [1,2,3]
    second_list = [1,2,3,4]
    return first_list,second_list

first_list,second_list=lists()
def N(first_list,second_list):
    firstN=len(first_list)
    secondN=len(second_list)
    if firstN==secondN:
        return "="
    elif firstN>secondN:
        return ">"
    else:
        return "<"
def indexC(first_list,second_list):
    greater=N(first_list,second_list)
    firstN=len(first_list)
    secondN=len(second_list)
    if greater=="=":
        for i in range(firstN):
            if first_list!=second_list: 
              return False  
    elif greater==">":
        for i in range(firstN):
            if first_list!=second_list: 
                return False
    elif greater=="<":
        for i in range(secondN):
            if first_list!=second_list: 
                return False
    return True
print(indexC(first_list,second_list))
def doublelooper_index(first_list,second_list):
    greater=N(first_list,second_list)
    firstN=len(first_list)
    secondN=len(second_list)
    match=0
    flag=indexC(first_list,second_list)
    if not flag:
        if greater=="=":
            for i in first_list:
                for j in second_list:
                    if i == j:
                        match+=1   
            return match/firstN *100
        elif greater==">":
            
            for i in first_list:
                for j in second_list:
                    if i == j:
                        match+=1
            return match/firstN*100
        elif greater=="<":
            for i in second_list:
                for j in first_list:
                    if i == j:
                        match+=1
            return match/secondN*100
    else:
        return "100% perfect match"
print(doublelooper_index(first_list,second_list))
#compares list if no repeatition is done