def is_prime(n): #used in later problems
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


#4.1
def print_list(l):
	print(*l)

def print_list_r(l):
	l.reverse()
	print(l)
	
def my_len(l):
	i = 0
	for j in l:
		i += 1
	return i
	
	
#4.2
a = [6,2,7,3,6]
b = a
b[1] = 10
#a changed as well
c = a[:] #its a copy
c[2] = 20
#a was unaffected


def set_first_elem_to_zero(l):
	l[0] = 0
	return l
#in this case the original list is affected
#count be avoided by cpying the list using [:]


#4.3
#b doesnt work as xrange() is not used in python 3
#if range() is used then the result is the same

#4.4 
def set_to_zero(l,i):
	l[i] = 0
	return l
	
#4.5
#see excercise 3

#4.6
#a
def gen_list(x,y):
	l = []
	for i in range(x):
		for j in range(y):
			l.append([i,j])
#b
def gen_list_2(x,y):	
	l = []
	for i in range(x):
		for j in range(i, y):
			l.append([i,j])
#c
def gen_list_3(x,y):
	for i in range(x):
		for j in range(i, y):
			if is_prime(i) and is_prime(j):
				l.append(i + j)
#d
def eval_arb_poly(x, coef):
	result = 0
	enum1 = enumerate(coef, 0)
	for i, j in enum1:
		result += (j * (x ** i))
	return result

print(eval_arb_poly(2, [4, 3, 2, 1])) #expected output: 26 

#4.7
'''
remove yield line and uncomment commented lines
to change return type from generator to list
'''
def my_filter(func, l):
	#result = []
	for i in l:
		if func(i):
			yield i
			#result.append(i)
	#return result
	
#4.8
def my_flatten(a):
	result = []
	for i in a:
		result += i
	return result
	
#4.9
import re #regex
def find_longest_words(my_string):
	result = []
	max = 0
	string_list = my_string.split(" ")
	regex = re.compile('[^a-zA-Z]')
	for i in range(len(string_list)):
		string_list[i] = regex.sub('', string_list[i])
	for j in string_list:
		if len(j) > max:
			max = len(j)
			result = [j]
		elif len(j) == max:
			result.append(j)
	return result
#TEST STRING expected output [variable, therable, scaries]
a = "this is a string of variable length, therable, scareies..."

#4.10	
def collatz(a):
	result = []
	while not a == 1:
		result.append(a)
		if not a % 2:
			a = a/2
		else:
			a = 3 * a + 1
			
	return result
	
def max_collatz(n):
	max_input = 0
	result = []
	max = 0
	for i in range(1, n):
		a = collatz(i)
		if len(a) >= max:
			max_input = i
			max = len(a)
			result = a[:]
			
	return max_input #for n=1,000,000 the result is 524
	
#4.11
def my_pivot(x, ys):
	below = []
	above = []
	for y in ys:
		if y <= x:
			below.append(y)
		else:
			above.append(y)
	below.append(x)
	below += above
	return below
	
#4.12
#FINAL 2 lines
def primes(n):
	lam1 = lambda y: [True if y % x else False for x in range(2,y)]
	return list(filter(lambda a: a != '',[y if not False in lam1(y) else "" for y in range(2,n)]))
	

	
	