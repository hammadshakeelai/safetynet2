f = [1,2,2,3]
s = [1,2,3]

match=0
for i in f:
    if i in s:
        match+=1
print((match-len(f))/len(f)*100)