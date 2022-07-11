



def solution1(*args,**kwargs):
    if len(args) == 2 :
        dict_result = {**dict1,**dict2}  
    elif len(args) == 3 : 
        dict_result = {**dict1,**dict2,**dict3}
    return dict_result




dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {'Sixty':60,'Sevnty':70}
print(solution1(dict1,dict2))
print(solution1(dict1,dict2,dict3))