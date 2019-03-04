def intensify(message,n):

    dict = (" very", " really", " so", " hella", " totally", " extremely", " Very", " Really", " So", " Hella", " Totally", " Extremely")

    #marks = {".": "!", "?": "?!", "!": "!!"}
    #marks = (".", "?", "!")
    #mark = ("!!", "?!", "!")
    
    for i in dict:
        message = message.replace(i, i*n)
    
    #for k, v in zip(marks, mark):
        #message = message.replace(k,v,1)
        
    message = message.replace(".","!")
    message = message.replace("!","!!")
    message = message.replace("?","?!")

        
    return message

    
        
        
        
