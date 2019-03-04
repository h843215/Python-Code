def word2dict(word):
    
    c = {}

    for character in word:
        c.setdefault(character, 0)
        c[character] = c[character] + 1
    return c

#print(word2dict('bee'))

def can_be_composed(word1,word2):

    dict2 = word2dict(word2)
    dict1 = word2dict(word1)

    for l in dict1:
        if l in dict2:
            if dict2.get(l) < dict1.get(l):
                return False
        else:
            return False
    return True
            
        
        
        
print(can_be_composed("bee", "be"))
            
            
        
        

    
    
    
    
        

