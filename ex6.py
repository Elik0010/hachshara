#6.1
def print_dict(d):
	for i in d.items():
		print(i)
	
#TEST CODE
d = {
	"one":1,
	"two":2,
	"three":3,
	"four":4,
	"five":5,
	"six":6
	}
	
#6.2
def hist(li):
	my_dict = {}
	for i in li:
		if  str(i) in my_dict:
			my_dict[str(i)] += 1
		else:
			my_dict[str(i)] = 1
		
	return list(my_dict.items())
	
import Collections as col
def hist2(li): #using counter in the collections library
	c = col.Counter()
	
	for i in li:
		c[str(i)] += 1
	return list(c.items())
	
#6.3
def hist3(li):
	my_dict = {}
	for i in li:
		if my_dict.get(str(i), 0):
			my_dict[str(i)] += 1
		else:
			my_dict[str(i)] = 1
		
	return list(my_dict.items())

#6.4


#6.5
#a
def dense_add(a, b):
	return a + b
#b	
def dense_multiply(a, b):
	return a * b
	

def convert_sparse_vec_to_dic(a):
	c = {}
	for i in range(len(a)):
		if a[i]: #if the value isnt zero
			c[i] = a[i]
	return c	
#c	
def sparse_add(a, b):
	if not isinstance(a,dict):
		a = convert_sparse_vec_to_dic(a)
	if not isinstance(b, dict):
		b = convert_sparse_vec_to_dic(b)
	for i in a:
		if i in b:
			b[i] += a[i]
		else:
			b[i] = a[i]
	return b
#d	
def sparse_multiply(a, b):
	if not isinstance(a, dict):
		a = convert_sparse_vec_to_dic(a)
	if not isinstance(b, dict):
		b = convert_sparse_vec_to_dic(b)
	'''
	result = b.copy()
	for i in a:
		if i in b:
			result[i] = a[i] * b[i]
	return result
	'''
	result = 0
	for i in a:
		if i in b:
			result += a[i] * b[i]
	return result
#e
def add_sparse_dense(sparse, dense):
	if not isinstance(sparse, dict):
		sparse = convert_sparse_vec_to_dic(sparse)
	result = dense[:] #copy of dense
	for i in sparse:
			result[i] += sparse[i]
	return result
	
#f
def multiply_sparse_dense(sparse,dense): #returns List
	if not isinstance(sparse, dict):
		sparse = convert_sparse_vec_to_dic(sparse)
	'''
	result =  [0 for i in dense] #array of zeros with the same length as dense
	for i in sparse:
			result[i] = sparse[i] * dense[i]
	return result
	'''
	result = 0
	for i in sparse:
		result += sparse[i] * dense[i]
	return result
	

	
