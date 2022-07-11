
'''
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''


def solution1(*args):
    result = dict(zip(keys,values))
    return result


def solution2(*args):
    result = {}
    for idx in range(len(keys)):
        result.update({keys[idx]: values[idx]})
    return result

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(solution1(keys,values))
print(solution2(keys,values))