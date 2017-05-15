
class GradientBoosting(object):
	def __init__(self, n_estimators, learning_rate, min_samples_split,
					min_impurity, max_depth, regression, debug):
		self.loss = SquareLoss()

		self.trees = []
		for _ in range(n_estimators):
			tree = RegressionTree(
					min_samples_split = self.min_samples_split,
					min_impurity = self.min_impurity,
					max_depth = self.max_depth
					)

	def fit(self, X, y):
		y_pred = np.full(np.shape(y), np.mean(y, axis=0))
		for i, tree in enumerate(self.trees):
			gradient = self.loss.gradient(y, y_pred)
			tree.fit(x, gradient)
			update = tree.predict(X)
			y_pred -= np.multiply(self.learning_rate, gradient)
			