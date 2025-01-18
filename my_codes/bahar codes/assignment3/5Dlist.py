my_list=[[[[1,0],[2,3]],[[4,2],[6,5]]],[[[5,6],[3,5]],[[2,7],[0,1]]]]

# mlist=[[4,7,9,4],[4,8,0,8],[4,7,9,4],[4,8,0,8]]

# print(mlist[1][3])
your_list=[[[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]],[[[[1,0],[2,3]],[[4,2],[6,5]]],[[[5,6],[3,5]],[[2,7],[0,1]]]]]
def indexinator ( my_list, index_list = [] ):
    if type ( my_list ) != list :
        print ( f'{ tuple( index_list ) }: { my_list }' )
    else:
        for i in range ( len( my_list ) ):
            new_index_list = index_list + [i]
            indexinator ( my_list[i], new_index_list )

indexinator(your_list)
# # indexinator=765
# # print(f'hjygtygrvdc{indexinator}k,umjynhtbgrvfecd')
# # print('thgfrdsa'+str(indexinator)+'oymnbthgfvdcs')