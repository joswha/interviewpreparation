def twoNumberSum(array, targetSum):
	table = {} # no need to use comprehension
	for elem in array:
		if targetSum - elem in table:
			return [elem, targetSum - elem]
		else:
			table[elem] = 1
	return []