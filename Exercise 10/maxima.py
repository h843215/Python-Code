def find_maxima(lst):  
    if lst == []:
        return lst
    lst1 = [lst[0]]
    c_max = lst[0]
    for x in lst:
        if x > c_max:
            c_max = x
            lst1.append(x)
    return lst1

#print(find_maxima([]))

