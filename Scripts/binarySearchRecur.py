def binSearch(arr, low, high, val):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binSearch(arr, low, mid-1, val)
        else:
            return binSearch(arr, mid+1, high, val)

    else:
        return -1

array = [1, 10, 14, 90]
searVal = 10

print(binSearch(array, 0, len(array)-1, searVal))
