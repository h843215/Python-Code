import re
def card2int(s):
    
    n1 = {'a':1,
        'one':1,
              'two':2,
              'three':3,
              'four':4,
              'five':5,
              'six':6,
              'seven':7,
              'eight':8,
              'nine':9,
              'ten':10,
              'eleven':11,
              'twelve':12,
              'thirteen':13,
              'fourteen':14,
              'fifteen':15,
              'sixteen':16,
              'seventeen':17,
              'eighteen':18,
              'nineteen':19,
              'twenty':20, 'thirty': 30, 'forty':40, 'fifty':50, 'sixty':60,
              'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100}

    n2 = {
          'thousand':1000,
          'million':1000000,
          'billion':1000000000,
          'trillion':1000000000000,
          'quadrillion':1000000000000000,
          'quintillion':1000000000000000000,
          'sextillion':1000000000000000000000,
          'septillion':1000000000000000000000000,
          'octillion':1000000000000000000000000000,
          'nonillion':1000000000000000000000000000000,
          'decillion':1000000000000000000000000000000000}

    sum = 0
    sum2 = 0
    q = re.compile(r'[^\W\s]?\w+')
    i = q.findall(s)
    if 'oh' in i:
        return None
    lst1 = []
    lst2 = []
    ans = 0
    for token in i:
        if token in n1.keys():
            if token == 'hundred':
                a = n1.get(token)
                sum *= a
            else:
                a = n1.get(token)
                sum += a
            lst1.append(sum)
        elif token in n2.keys():
            b = n2.get(token)
            sum2 = sum*b
            lst2.append(sum2)
            sum = 0            

    for element in lst2:
        ans += element
            #print(ans)
    ans += lst1[-1]
    
    if 'negative' in i:
        ans = ans*-1
    return ans
