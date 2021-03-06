
'''
    Given a two Python list. Write a program to
    iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

    Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100
'''




from ntpath import join


def solution1(*args):
    res = list(zip(list1,list2[::-1]))
    for idx in range(len(res)):
        print(res[idx])
    # return ('\n'.join(map(str,res)))

def solution2(*args):
    for x,y in zip(list1,list2[::-1]):
        print(x,y)


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
solution1(list1,list2)
solution2(list1,list2)