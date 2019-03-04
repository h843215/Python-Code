def find_opposites(lst):
    
    dict = {}
    dict2 = {}
    c = 0
    for k in lst:
        dict[k] = c
        #print(dict)
        if k in dict:
            dict2[k] = k[::-1]
            #dict2[k] = "".join((k.split().reverse()))
            #print(dict2)
            if k == dict2[k]:
                del dict2[k]
            elif k[::-1] not in lst:
                del dict2[k]
            elif k > dict2[k]:
                del dict2[k]
    return list(dict2.items())
    
#print(find_opposites_quickly([ "according", "deer", "net", "ten", "reed", "refer", "raw", "war", "addition", "frequency", "platform" ]))
#print(find_opposites_quickly([]))
#print(find_opposites_quickly(["abba"]))
#print(find_opposites_quickly(["deer", "reed"]))
    

    
    
