#Concatenate two lists in the following order

def solution1(*args):
    result = []
    for idx in range(len(list1)):
        for idy in range(len(list2)):
            res = list1[idx] + list2[idy]
            result.append(res)
    # res = [x + y for x in list1 for y in list2]
    return result


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print(solution1(list1,list2))