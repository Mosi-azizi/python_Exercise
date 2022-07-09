# Write a program (function!) that takes a list and returns a 
# new list that contains all the elements of the first list minus all the duplicates.
def solution(L):
    B=[]
    for item in L:
        if item not in B:
            B.append(item)
    return B

L= [2,3,4,4,4,4,76,7,8,76]
print(solution(L))