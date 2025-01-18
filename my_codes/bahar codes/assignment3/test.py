my_list=[[[[1,0],[2,3]],[[4,2],[6,5]]],[[[5,6],[3,5]],[[2,7],[0,1]]]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        for k in range(len(my_list[i][j])):
            for l in range(len(my_list[i][j][k])):
                print('(',i,',',j,',',k,',',l,')',my_list[i][j][k][l])
# my_list=[2,46,9,5,3,1,-1]
# smallest_i = my_list[0]
# for i in my_list:
#     if i <smallest_i:
#         smallest_i = i

# print(smallest_i)

# def indexinator(my_list,list1=[]):
#     if type(my_list)==list:
#         for i in range(len(my_list)):
#             indexinator(my_list[i],list1+[i])
#     else:
#         print(f'({list1}):{my_list}')
    
# indexinator(my_list)