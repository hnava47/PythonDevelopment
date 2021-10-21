def custMin(paramList):

    n = len(paramList)-1

    for pos in range(n):
        if paramList[pos] < paramList[pos+1]:
            paramList[pos], paramList[pos+1] = paramList[pos+1], paramList[pos]

    return paramList[n]

print(custMin([5, 2, 9, 10, -2, 90]))
