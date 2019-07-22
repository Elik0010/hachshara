#5.1
#no activities here
#5.2

def zip_lists_manual(x,y):
	result = []
	for i in range(len(x)):
		result.append((x[i], y[i]))
	return result

def zip_lists_automatic(x,y):
	return list(zip(x,y))


def unzip_manual(zipped):
	x = [i[0] for i in zipped]
	y = [i[1] for i in zipped]
	return x, y

x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(x)
print(y)
a = zip_lists_manual(x, y)
print(a)

x, y = unzip_manual(a)
print(x)
print(y)


#5.3

'''
The L1 norm that is calculated as the 
sum of the absolute values of the vector.
The L2 norm that is calculated as the 
square root of the sum of the squared vector values.
'''
import math
def get_distance_l1(x, y):
	result = 0
	for i in range(len(x)):
		result += abs(x[i] - y[i])
	return result


def get_distance_l2(x, y):
	result = 0
	for i in range(len(x)):
		result += (x[i] - y[i]) ** 2
	print(result)
	return math.sqrt(result)


#TEST CODE
x = [1,2,3]
y = [10,5,15]
print(get_distance_l1(x,y)) #expected output - 24
print(get_distance_l2(x,y)) #expected output - 15.29