#13.1
def collatz_gen(n):
    while n != 1: 
        yield n
        if n % 2: #if n is odd
            n = 3 * n + 1
        else: #n is even
            n = n // 2



hi = collatz_gen(103)

try:
    while True:
        print(hi.__next__())
except:
    print("DONE")

#13.2
vec = []
vecgen = collatz_gen(61)
try:
    while True:
        vec.append(vecgen.__next__())
except:
    print("DONE")
    print(vec)

#13.3
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


def prime_gen(n):
    if n:
        yield 2
        n -= 1
    if n:
        yield 3
        n -= 1
    curr = 5
    while n:
        if is_prime(curr):
            yield curr
            n -= 1
        if n:
            if is_prime(curr + 2):
                yield curr + 2
                n -= 1
        curr += 6


primg = prime_gen(10000)

try:
    while True:
        print(primg.__next__(), end = '-')
except:
    print("Done")