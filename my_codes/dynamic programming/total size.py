str1='hyhouseesuohyh'    
for i in range(1,len(str1)+1):
    if str1[:i]==str1[:i][::-1]:
        print(f'{str1[:i]} is a palindrome')
