# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return binSearch(array, 0, len(array)-1, target)

def binSearch(array, low, high, value):
    mid = high + low // 2

    if low <= high:
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return binSearch(array, mid+1, high, value)
        elif array[mid] > value:
            return binSearch(array, low, mid-1, value)
    else:
        return -1
