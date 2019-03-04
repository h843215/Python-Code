import re

def tokenize(text):

    text = text.replace("n't", " n't")
    s = re.compile(r'\'\w|Mr\.|Ms\.|Mrs\.|Dr\.|n\'t|[.,!?;:""]|\w+')
    result = s.findall(text)
    return result

#print(tokenize('Mr. Brown opened the door and said with a smile, "I can\'t believe it! It\'s such a pleasure to see you!"'))
    
