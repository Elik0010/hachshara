import sys
class RangeError(Exception):
    pass

def is_prime(n):
	if n == 1 or n == 0:
		return False
	if n == 2 or n == 3:
		return True
	if not n % 2 or not n % 3:
		return False
	for i in range(5, n // 2 + 2, 6):
		#Checking every possible prime number up until half of the subject
		if not n % i:
			return False
		if not n % (i+2):
			return False
	return True

def between_primes(a, b):
    try: 
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError#("these are not both ints \n")
        if a > b:
            raise RangeError("a cannot be lower than b \n")
        result = []
        for i in range(a,b):
            if is_prime(i):
                result.append(i)
        return result
    except(Exception) as e:
       print("%serror occured" % e)
        
print(is_prime(49))
