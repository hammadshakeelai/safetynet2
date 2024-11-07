list=[8,9,6,9,8,6,1,7,7,9,9,1,5,5,21,8,8]
size=len(list)
for i in range(size):#len i loop
     flag=True
     for j in range(size):#len j loop
          if list[i]==list[j] and i!=j:#if list[j]=list[i] and on diferent indexes
               flag=False#               break outer loop
               break#                     break inner loop
          if i!=j and list[i]!=list[j]:# diferent indexes but values not equal
             x=list[i]#value not paired is stored here
     if not flag:
          continue 
     else:
          break
print(x)