
#   Write a program that takes a list of numbers
#  (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
def solution(L):
    first = L[0]
    end = L[-1]
    newList = [first,end]
    return newList

L= [2,3,4,4,4,4,76,7,8,76]
print(solution(L))
