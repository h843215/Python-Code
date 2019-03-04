def sum_except(start, end, omit = None):
    result = 0
    for n in range(start, end+1):
        result = result + n
    if omit != None:
        result = result-omit
    return result


def sum_step(start, end, step = 1):
    result = 0
    for n in range(start, end+1, step):
        result = result + n
                
    return result

            
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            i += 1
    return True

def find_biggest_prime(n):
    for i in range(n,2,-1):
        if is_prime(i):
            return i
    return None
    
