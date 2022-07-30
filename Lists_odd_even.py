def member_odd_even(mylist):
    odd_list = []
    even_list = []
    for idx in range(len(mylist)):
        if mylist[idx] % 2 == 0 :
            even_list.append(mylist[idx])
        else:
            odd_list.append(mylist[idx])
    print(even_list,odd_list)
    for x,y in zip(even_list,odd_list):
        print(x,y)
    

mylist = [234,445,55,36,326,32,67,1]
member_odd_even(mylist)




if __name__ == 'main':
    member_odd_even(mylist)