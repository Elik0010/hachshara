import numpy as np
class OLS:
	def __init__(self):
		self.coef = None
		self.bias = None
	
	def fit(self, x, y):
		self.coef = (len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
		(len(x) * np.sum(x * x) - np.sum(x) ** 2)
		self.bias = (np.sum(y) - self.coef * np.sum(x)) / len(x)
	
		return self.coef, self.bias
	def predict(self, x):
		return self.coef * x + self.bias
	
	def model_summary(self):
		print("model: %sx + %s" % (self.coef,self.bias))
		
	
	
#TEST CODE
ols = OLS()
a = np.array([1,2,3,4,5,6,7,8])
b = np.array([100,132,176,145,190,240,280,300])
c, d = ols.fit(a,b)
vec = np.arange(10)
ols.model_summary()
print(ols.predict(10))