my_list=[[[[1,0],[2,3]],[[4,2],[6,5]]],[[[5,6],[3,5]],[[2,7],[0,1]]]]


your_list=[[[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]],[[[[1,0],[2,3]],[[4,2],[6,5]]],[[[5,6],[3,5]],[[2,7],[0,1]]]]]


def indexinator ( my_list, index_list = [] ):
    if type ( my_list ) != list :
        print ( f'{ tuple( index_list ) }: { my_list }' )
    else:
        for i in range ( len( my_list ) ):
            new_index_list = index_list + [i]
            indexinator ( my_list[i], new_index_list )

indexinator(your_list)

