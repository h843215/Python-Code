def positivize(review):
    
    dict = {"bad": "good", "horrible": "fantastic", "dirty": "clean", "disgusting": "sublime", "expensive": "affordable", "moldy": "flavourful", "frozen": "farm-fresh", "Bad": "Good", "Horrible": "Fantastic", "Dirty": "Clean", "Disgusting": "Sublime", "Expensive": "Affordable", "Moldy": "Favourful", "Frozen": "Farm-fresh"}

     
    for k, v in dict.items():
        review = review.replace(k,v)
    s = review.split(' ')
    for i in s:
        if i.isdigit():
            j = int(i)/2
            review = review.replace(i, "only " + str(int(j)))
    return review

print(positivize("The food was horrible!!! We waited 40 minutes for frozen vegetables and moldy bread. Disgusting!"))
        
        
        
