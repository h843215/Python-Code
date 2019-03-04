def sort(words):

    word = []

    while words != []:
        minimum = min(words)
        #minimum = words[0]
        #for i in words:
            #if i < minimum:
                #minimum = i
        word.append(minimum)
        words.remove(minimum)

    while word != []:
        minimum = min(word)
        words.append(minimum)
        word.remove(minimum)

#print(sort(['pineapple', 'annanas', 'burger', 'pear', 'mango', 'apple', 'orange']))

    

        
        
