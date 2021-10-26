def tournamentWinner(competitions, results):
    # Write your code here.
	compSet = set()
	for comp in range(len(competitions)):
		compSet.add(competitions[comp][0])
		compSet.add(competitions[comp][1])

	compDict = {value: 0 for value in compSet}
	for idx in range(len(results)):
		if results[idx] == 0:
			compDict[competitions[idx][1]] += 3
		elif results[idx] == 1:
			compDict[competitions[idx][0]] += 3

    # Returns key with largest value
	return max(compDict, key=compDict.get)
