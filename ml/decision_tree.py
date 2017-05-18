# copy paste learning from:
# https://github.com/eriklindernoren/ML-From-Scratch/blob/master/supervised_learning/decision_tree.py

class decisionNode():
	def __init__(self):
		self.feature_i = feature_i # index of feature being tested
		self.threshold = threshold # 
		self.value = value # if leave node
		self.true_branch # left node
		self.false_branch #right node

def DecisionTree():
	def __init__():
		self.root = None
		self.min_samples_split = min_samples_split
		self.min_impurity = min_impurity
		self.max_depth = max_depth
		self._impurity_calculation = None
		self._leaf_value_calculation = None
		self.one_dim = None
		self.loss = loss

	def fit(self, X, y):
		self.one_dim
		self.root = self._build_tree(X, y)

	def _build_tree(self, X, y):
		largest_impurity = 0
		best_criteria = None
		best_sets = None
		X_y = np.concatenate((X,y), axis=1)
		n_samples, n_features = np.shape(X)

		if n_samples >= self.min_samples_split and current_depth <= self.max_depth:
			for feature_i in range(n_features):
				feature_values = np.expand_dims(X[:, feature_i], axis=1)
				unique_values = np.unique(feature_values)
				for threshold in unique_values:
					Xy1, Xy2 = divide_on_feature(X_y, feature_i, threshold)
					if len(Xy1) > 0 and len(Xy2) > 0:
						y1 = Xy1[:, n_features:]
						y2 = Xy2[:, n_features:]
						impurity = self._impurity_calculation(y, y1, y2)
						if impurity > largest_impurity:
							largest_impurity = impurity
							best_criteria = {"feature_i": feature_i, "threshold":threshold}
							best_sets = {
								"leftX": Xy1[:, :n_features],
								"leftY": Xy1[:, n_features:],
								"rightX": Xy2[:, :n_features],
								"rightY": Xy2[:, n_features:]
							}

		if largest_impurity > self.min_impurity:
			true_branch  = self._build_tree(best_sets['leftX'], best_sets['lefty'], current_depth+1)
			false_branch = self._build_tree(best_sets['rightX'],best_sets['righty'],current_depth+1)
			return DecisionNode(feature_i = best_criteria['feature_i'],
								threshold = best_criteria['threshold'],
								true_branch = true_branch, 
								false_branch = false_branch)

		leaf_value = self._leaf_value_calculation(y)
		return DecisionNode(value=leaf_value)

def ClassificationTree(DecisionTree):
	def _calculate_infomation_gain(self, y, y1, y2):
		p = len(y1) / len(y)
		entropy = entropy(y)
		info_rain = entropy - p*entropy(y1) - (1-p)*entropy(y2)
		return info_gain
	def _majority_vote(self, y):
		most_common = None
		max_count = 0
		for label in np.unique(y):
			count = len(y[y==label])
			if count > max_count:
				most_common = label
				max_count = count
		return most_common
	def fit(self, X, y):
		self._impurity_calculation = self._calculate_infomation_gain
		self._leaf_value_calculation = self._majority_vote
		super(ClassificationTree, self).fit(X,y)

def RegressionTree(DecisionTree):
	def _calculate_variance_reduction(self, y, y1, y2):
		var_tot = calculate_variance(y)
		var_1 = calculate_variance(y1)
		var_2 = calculate_variance(y2)
		frac_1 = len(y1)/len(y)
		frac_2 = len(y2)/len(y)
		variance_reduction = var_tot - (frac_1*var1 + frac_2*var_2)
		return sum(variance_reduction)
	def _mean_of_y(self, y):
		value = np.mean(y)
		return value if len(value)>1 else value[0]
	def fit(self, X, y):
		self._impurity_calculation = self._calculate_variance_reduction
		self._leaf_value_calculation = self._mean_of_y
		super(RegressionTree, self).fit(X, y)

def XGBoostRegressionTree(DecisionTree):
	def _split(self, y):
		col = int(np.shape(y)[1]/2)
		y, y_pred = y[:, :col], y[:, col:]
		return y, y_pred
	def _gain(self, y, y_pred):
		nominator   = np.power(self.loss.gradient(y, y_pred).sum(), 2)
		denominator = self.loss.hess(y, y_pred).sum()
		return 0.5 * (nominator/denominator)
	def _gain_by_taylor(self, y, y1, y2):
		y, y_pred = self._split(y)
		y1, y1_pred = self.split(y1)
		y2, y2_pred = self.split(y2)
		true_gain = self._gain(y1, y1_pre)
		false_gain = self._gain(y2, y2_pre)
		gain = self._gain(y, y_pred)
		return true_gain + false_gain - gain
	








