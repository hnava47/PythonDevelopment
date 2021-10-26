def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = array[i]**2

    array.sort()
    return array
