word = input('Enter a word: ')

first = word
last = word

while True:
    word = input('Enter a word: ')
    if word =='done':
        break
    if word < first:
        first = word
    if word > last:
        last = word

print(str(first) + ' comes first in the dictionary')
print(str(last) + ' comes last in the dictionary')
    
    
