import random
import numpy as np
from sklearn.datasets import load_iris

class LinearRegression():
	
	def __init__(self, n_iter=100, learning_rate=0.01, gradient_descent=True):
		self.w = None
		self.n_iter = n_iter
		self.learning_rate = learning_rate
		self.gradient_descent = gradient_descent
		
	def fit(self, X, y):
		X = np.insert(X, 0, 1, axis=1)
		if self.gradient_descent:
			n_features = np.shape(X)[1]
			self.w = np.random.random((n_features,))
			for _ in range(self.n_iter):
				w_gradient = X.T.dot(X.dot(self.w)-y)
				self.w -= self.learning_rate*w_gradient
				
	def predict(self, X):
		X = np.insert(X, 0, 1, axis=1)
		y_pred = X.dot(self.w)

def loadData():
	iris = load_iris()
	return np.array(iris.data)

#def main():
data = loadData()
clr = LinearRegression()
X = data[:,:3]
y = data[:,3:]
clr.fit(X,y)

if __name__ == "__main__":
	main()