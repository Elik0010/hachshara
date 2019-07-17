import math
class Rational:
	def __init__(self, p = 1, q = 1):
		self.nominator = p
		self.denominator = q
		self.simplify()
		
	def __str__(self):
		return "%s/%s" % (self.nominator, self.denominator)
	
	def __add__(self, other):
		if not isinstance(other, Rational): #assuming other is an integer
			other = Rational(self.denominator * other, self.denominator)
		if self.denominator == other.denominator:
			return Rational(self.nominator + other.nominator, self.denominator)
		nom = (self.nominator * other.denominator) + (other.nominator * self.denominator)
		denom = self.denominator * other.denominator
		return Rational(nom, denom)
		
	def __sub__(self, other):
		if not isinstance(other, Rational): #assuming other is an integer
			other = Rational(self.denominator * other, self.denominator)
		if self.denominator == other.denominator:
			return Rational(self.nominator - other.nominator, self.denominator)
		nom = (self.nominator * other.denominator) - (other.nominator + self.denominator)
		denom = self.denominator * other.denominator
		return Rational(nom, denom)
			
	def __mul__(self, other):
		if not isinstance(other, Rational): #assuming other is an integer
			other = Rational(self.denominator * other, self.denominator)
		nom = self.nominator * other.nominator
		denom = self.denominator * other.denominator
		return Rational(nom,denom)
	
	def __truediv__(self, other):
		if not isinstance(other, Rational): #assuming other is an integer
			other = Rational(self.denominator * other, self.denominator)
		nom = self.nominator * other.denominator
		denom = self.denominator * other.nominator
		return Rational(nom,denom)
		
	def __eq__(self, other):
		if self.nominator == other.nominator \
		and self.denominator == other.denominator:
			return True
		return False
		
	def __float__(self):
		return self.nominator / self.denominator
	
	def simplify(self):
		for i in (range(min(self.nominator, self.denominator), 1,  -1)):
			if not self.nominator % i and not self.denominator % i:
				self.nominator //= i
				self.denominator //= i
				break
				
	
c = Rational(2,5)
d = Rational(4,10)
print(float(c))