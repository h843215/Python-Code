def product(nums):
	if not nums:
		return 1
	return nums[0] * product(nums[1:])

#print(product([2, 3, 1, -5, 3]))

def squares(nums):
	if nums == 0:
		return 0
	else:
		s = list(map(lambda x: x ** 2, nums))
		return s
		
#print(squares([-2,-1, 0, 1, 2, 5]))

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    def f(n,k):
        if k*k > n:
            return True
        elif n % k == 0:
            return False
        else:
            return f(n, k + 2)
    return f(n, 3)

#print(is_prime(8413))
	
    
    
