def solution(L):
    B=[]
    for item in L:
        if item not in B:
            B.append(item)
    return B

L= [2,3,4,4,4,4,76,7,8,76]
print(solution(L))