def solution_1(A):
    unpaired = 0
    for number in A:
        unpaired ^= number
    return unpaired#/

def solution_2(A):
    from collections import defaultdict
    count = defaultdict(int)
    for number in A:
        count[number] += 1
    for number, freq in count.items():
        if freq % 2 != 0:
            return number#/
        
def solution(A):
    from collections import Counter
    counts = Counter(A)
    for number, freq in counts.items():
        if freq == 1:
            return number#/
        
def solution_3(A):
    A.sort()
    for i in range(0, len(A) - 1, 2):
        if A[i] != A[i + 1]:
            return A[i]
    return A[-1]#/

def solution_4(A):
    for number in A:
        if A.count(number) == 1:
            return number#/
        
def solution(A):
    from functools import reduce
    return reduce(lambda x, y: x ^ y, A)#/

def solution(A):
    unpaired_elements = set()
    for number in A:
        if number in unpaired_elements:
            unpaired_elements.remove(number)
        else:
            unpaired_elements.add(number) 
    return unpaired_elements.pop() #///


A = [21, 9, 3, 9,8,7, 3, 9, 7, 9, 9, 7, 21,9,8]
print(solution_3(A))
