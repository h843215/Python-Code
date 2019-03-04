from fragments import get_random_text

def easy_password(length):
    pwd = ""
    while len(pwd) != length:
        pwd = ""
        while len(pwd) < length: 
            pwd = pwd + get_random_text()
        
    return pwd
        
