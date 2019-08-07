#3.1
def hello():
	print("Hello World!")
	
def hello_name(name):
	print("Hello, %s!" % (name))
	
#return can save the value into a variable and doesnt display it to the window
#whereas print will display the data on the terminal


#3.2
def eval(x):
	print(3 * (x ** 2) - x + 2)
	
	
#3.3
def my_max(x, y):
	if x < y:
		print(y)
	if y <= x:
		print(x)
def my_max(x, y):
	if x < y:
		print(y)
	else:
		print(x)
		

#3.4	
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
	

def all_primes(n): #UPDATED for 4.5
	l = []
	if n > 2:
		l.append(2)
		#print(2)
	if n > 3:
		l.append(3)
		#print(3)
		
	for i in range(5, n, 6):
		if is_prime(i):
			l.append(i)
			#print(i)
		if(is_prime(i+2)):
			l.append(i+2)
			#print(i+2)
	return l
			
def first_primes(n):
	o = n
	if o:
		print(2)
		o -= 1
	if o:
		print(3)
		o -= 1
	curr = 5
	while o:
		if is_prime(curr):
			print(curr)
			o -= 1
		if o:
			if is_prime(curr +2):
				print(curr + 2)
				o -= 1
		curr += 6
		
#3.5
def root(f, a, b): #using false position
	if (a >= 0 and b >= 0) or (a < 0 and b < 0):
		print("function evals have the same sign")
	top = a * f(b) - b * f(a)
	bottom = f(b) - f(a)
	c = top / bottom
	c = round(c, 5)
	print(c)
	return c
	#TODO figure out how to utilise with polynomials
	
	
def funct(x): #example function
	return x ** 2 + 15 * x	



print(all_primes(55))

