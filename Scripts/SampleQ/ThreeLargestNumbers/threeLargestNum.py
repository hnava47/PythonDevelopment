def findThreeLargestNumbers(array):
    # Write your code here.
	numList = [None, None, None]
	for i in array:
		compareThreeLargest(i, numList)
	return numList

def compareThreeLargest(num, numList):
	if numList[2] is None or num > numList[2]:
		updateList(num, 2, numList)
	elif numList[1] is None or num > numList[1]:
		updateList(num, 1, numList)
	elif numList[0] is None or num > numList[0]:
		updateList(num, 0, numList)

def updateList(num, idx, array):
	for i in range(idx+1):
		if idx == i:
			array[i] = num
		else:
			array[i] = array[i+1]

# def findThreeLargestNumbers(array):
#     # Write your code here.
# 	ordArray = []
# 	# O(n)
# 	for idx in range(3):
# 		maxInt = array.pop(array.index(max(array)))
# 		ordArray.append(maxInt)

# 	return ordArray[::-1]
