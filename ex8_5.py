import random
class mySet:
	def __init__(self, items = None):
		items = items or {}
		self.items = items
		self.length = len(items.items())

	def add(self, other):
		if other in self.items.values():
			return
		self.items[self.length] = other
		self.length += 1

	def clear(self):
		self.items.clear()
		self.length = 0		

	def copy(self):
		return mySet(self.items.copy())

	def difference(self, other):
		result = mySet()
		for i in self.items.values():
			if not i in other.items.values():
				result.items.add(i)
		return result

	def difference_update(self, other):
		for i in self.items.items():
			if self.items[i] in other.items.values():
				self.discard(i)
		return

	def discard(self, item):
		deletion_index = -1
		for i in self.items.keys():
			if item == self.items[i]:
				deletion_index = i
				break
		if deletion_index == -1:
			return deletion_index 
		#slide all the values down to fill over deleted element
		for i in range(deletion_index, self.length - 1):
			self.items[i] = self.items[i + 1]
		del self.items[self.length - 1]
		self.length -= 1
		return 0

	def intersection(self, *sets): 
		result = mySet()
		for i in self.items.values():
			in_all = True
			for set_i in sets:
				if not i in set_i.items.values():
					in_all = False
					break
			if in_all:		
				result.add(i)
		return result

	def intersection_update(self, *others):
		tostay = self.intersection(self, *others)
		self.__dict__ = tostay.__dict__
		return

	def isdisjoint(self, other):
		for i in self.items.values():
			if i in other.items.values():
				return False
		return True

	def issubset(self, other):
		for i in self.items.values():
			if not i in other.items.values():
				return False
		return True

	def issuperset(self, other):
		for i in other.items.values():
			if not i in self.items.values():
				return False
		return True

	def pop(self):
		rand = random.randrange(self.length)
		result = self.items[rand]
		self.discard(result)
		return result

	def remove(self, item):
		result = self.discard(item)
		if result == -1:
			raise Exception("Item not found in set")

	def symmetric_difference(self, other):
		result = mySet()
		list1 = list(self.items.values())
		list2 = list(other.items.values())
		combo = list2 + list1

		for i in combo:
			if i in list1 and i in list2:
				continue
			else:
				result.add(i)
		return result

	def symmetric_difference_update(self, other):
		result = self.symmetric_difference(other)
		self.__dict__ = result.__dict__
		return

	def union(self, other):
		result = self.copy()
		for i in other.items.keys():
			result.add(other.items[i])
		return result

	def update(self, other):
		result = self.union(other)
		self.__dict__ = result.__dict__

	def __str__(self):
		output = "{ "
		for i in self.items.values():
			output += 	i
			output +=", "
		output = output[:-2]
		output +="}"
		return "%s  %s" % (output, self.length)
