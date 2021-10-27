# O(n) time | O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
	result = []
	for num in array:
		offset = targetSum - num
		if offset in array:
			result = [offset, num]
	return result

# def twoNumberSum(array, targetSum):
#     for i in range(len(array)-1):
# 		for k in range(i+1, len(array)):
# 			if array[i] + array[k] == targetSum:
# 				return [array[i], array[k]]
# 	else:
# 		return []
