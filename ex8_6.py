class BinTree:
	def __init__(self, value):
		self.root = Node(value, 0)
		
	def __str__(self):
		total_result = []
		line = ""
		queue = [self.root, "\n"]
		while queue:
			i = queue[0]
			if isinstance(i, Node):
				line += str(i.value) + " "
				queue.append(i.l_child if i.l_child else "[] ")
				queue.append(i.r_child if i.r_child else "[] ")
				
			else:
				line += i
				if i == "[] ":
					queue.append("[] ")
					queue.append("[] ")
				elif i == "\n":
					end = True
					for j in queue:
						if isinstance(j, Node):
							end = False
							break
							
					if end:
						print("DONE")
						return line
					else:
						queue.append("\n")
			del	queue[0]		
	def insert(self, value, key):
		ins = Node(value, key)
		self.root.insert(ins)
	
	def search(self, key):
		return self.root.search(key)
	
	def remove(self, key):
		return self.root.remove(key)
			


class Node:
	def __init__(self, value, key, parent = None):
		self.key = key
		self.value = value
		self.l_child = None
		self.r_child = None
		self.parent = parent
	def insert(self, node):
		node.parent = self
		if node.key == self.key:
			self.value = node.value
			return
		if node.key < self.key:
			if self.l_child:
				self.l_child.insert(node)
			else:
				self.l_child = node
		else:
			if self.r_child:
				self.r_child.insert(node)
			else:
				self.r_child = node
	def search(self, key):
		if self.key == key:
			return self.value
		if key < self.key and self.l_child:
			return self.l_child.search(key)
		elif key > self.key and self.r_child:
			return self.r_child.search(key)
	
	def remove(self, key):
		togo = None
		if self.key == key:
			if not (self.l_child or self.r_child):
				if self.parent.l_child == self:
					self.parent.l_child = None
				else:
					self.parent.r_child = None
			elif self.l_child and self.r_child:
				temp = self.r_child
				while temp.l_child:
					temp = temp.l_child
				self.value = temp.value
				self.key = temp.key
				self.r_child.remove(temp.key)
				#TODO
				
			elif self.l_child:
				self.__dict__ = self.l_child.__dict__.copy()

			else:
				self.__dict__ = self.r_child.__dict__.copy()
		
		elif self.key > key and self.l_child:
			self.l_child.remove(key)
		elif self.key < key and self.r_child:
			self.r_child.remove(key)
		else:
			print("there is nothing to remove")
		

		
			