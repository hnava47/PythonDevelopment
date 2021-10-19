def custSort(listParam, sortType = 'asc'):
    listSet = set(listParam)
    sortList = []

    for setVal in listSet:
        count = 0
        position = 0
        dupList = []
        for listVal in listParam:
            if setVal == listVal and count < 1:
                count += 1
            elif setVal == listVal and count >= 1:
                count += 1
                dupList += [setVal]
            elif setVal > listVal:
                position += 1

        sortList.insert(position, setVal)

        for dupVal in dupList:
            dupPos = sortList.index(dupVal) + 1
            sortList.insert(dupPos, dupVal)

    if sortType.lower() == 'desc':
        return sortList[::-1]
    if sortType.lower() == 'asc':
        return sortList
    else:
        raise ValueError('Incorrect Sort Type')


print(custSort([8, 4, 2], 'desc'))
