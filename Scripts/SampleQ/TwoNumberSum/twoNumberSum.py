def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
		for k in range(i+1, len(array)):
			if array[i] + array[k] == targetSum:
				return [array[i], array[k]]
	else:
		return []
