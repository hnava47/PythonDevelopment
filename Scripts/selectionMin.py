def custMin(paramList):
    sortList = []

    sortList.append(min(paramList))

    paramList.pop(paramList.index(min(paramList)))

    return sortList[0]

print(custMin([3, 10, 8, 5, 3, -10]))
