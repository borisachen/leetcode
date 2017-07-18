def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def sigmoid_gradient(x)
	return sigmoid(x)*(1-sigmoid(x))

class LogisticRegression():
	def __init__(self, learning_rate=0.1, gradient_descent=True):
		self.param = None
		self.learning_rate = learning_rate
		self.gradient_descent = gradient_descent
	def fit(self, X, y, n_iterations=4000):
		X = np.insert(X, 0, 1, axis=1)
		n_samples, n_features = np.shape(X)
		a = -1 / math.sqrt(n_features)
		b = -a
		self.param = (b-a)*np.random.random((n_features,))+a
		for i in range(n_iterations):
			y_pred = sigmoid(X.dot(self.param))
			if self.gradient_descent:
				self.param -= self.learning_rate * X.T.dot(y_pred-y)
