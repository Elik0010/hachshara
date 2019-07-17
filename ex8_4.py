class Vector:
	def __add__(self,other):
		if isinstance(other, Sparse):
			return self.add_sparse(other)
		else:
			return self.add_dense(other)
			
	def __mul__(self, other):
		if isinstance(other, Sparse):
			return self.multiply_sparse(other)
		else:
			return self.multiply_dense(other)
	def multiply_dense(self, other):
		raise NotImplementedError()
	
	def multiply_sparse(self, other):
		raise NotImplementedError()
	
	def add_dense(self, other):
		raise NotImplementedError()
		
	def add_sparse(self, other):
		raise NotImplementedError()
	

class Sparse(Vector):
	def __init__(self, items = dict()):
		self.items = items # items should be a dictionary
	
	def __str__(self):
		return "%s" % (self.items)

			
	def add_sparse(self, other):
		result = Sparse(self.items.copy())
		print(result)
		for index, value in other.items.items():
			result.add(index, value)
		return result
	def add_dense(self, other):
		result = Dense(other.items[:])
		for index, value in self.items.items():
			result.items[index] += value
		return result
		
	def add(self, index, value):
		if self.items.get(index) == None:
			self.items[index] = value
		else:
			self.items[index] += value
			
			
	def multiply_sparse(self, other):
		result = 0
		for index, value in self.items.items():
			if not other.items.get(index) == None:
				result += other.items[index] * value
		return result
		
	def multiply_dense(self, other):
		result = 0
		for index, value in self.items.items():
			result += value * other.items[index]
		return result
		

		
		
		
		
	
	
	
	
class Dense(Vector):
	def __init__(self, items = []):
		self.items = items #items should be a list
		
	def __str__(self):
		return "%s" % (self.items)
	
	def add_dense(self, other):
		result = self.items[:]
		for i in range(len(other.items)):
			result[i] += other.items[i]
		return result

	def add_sparse(self, other):
		result = self.items[:]
		for index, value in other.items.items():
			result[index] += value
		return result
		
	def multiply_dense(self, other):
		result = 0
		for i in range(len(self.items)):
			result += self.items[i] * other.items[i]
		return result
	
	def multiply_sparse(self, other):
		result = 0
		for index, value in other.items.items():
			result += self.items[index] * value
		return result
		
		
		
#TEST CODE
a = Sparse({1:5,3:8,5:9})
c = Dense([1,4,6,7,9,8,2])
