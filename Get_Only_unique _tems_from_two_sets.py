
'''
Write a Python program to return a new set with unique items from both sets by removing duplicates.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
'''



def solution1(*args):
    set1.update(set2)
    return set1

def solution2(*args):
    set1.union(set2)
    return set1

set1 = {10, 20, 30, 40,50,50}
set2 = {30, 40, 50, 60, 70}
print(solution1(set1,set2))
print(solution2(set1,set2))
