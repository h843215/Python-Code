def find_opposites_quickly(lst):
    l = []
    dict = {}
    dict2 = {}
    for k in lst:
        dict[k] = 0
    for k in lst:
        dict2[k] = k[::-1]
        if k != dict2[k] and dict2[k] in dict:
            l.append((k,dict2[k]))
            del dict[k]
            del dict[dict2[k]]
    #elif dict2[k] not in dict.keys():
        #del dict2[k]
    return l
    
#print(find_opposites_quickly([ "according", "deer", "net", "ten", "reed", "refer", "raw", "war", "addition", "frequency", "platform" ]))
#print(find_opposites_quickly([]))
#print(find_opposites_quickly(["abba"]))
#print(find_opposites_quickly(["deer", "reed"]))
    
