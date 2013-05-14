def bubbleSort(array):
    changed = True
    length=len(array)
    while changed:
        changed = False
        for i in range(length-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                changed = True
    return array

def insertSort(array):
    length=len(array)
    for i in range(1, length):
        key = array[i]
        j = i    
        while j > 0 and array[j-1] > key:
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
    return array

def selectPivotLocation(array):
    return 0

def quickSort(array):
    if array==[]:
        return array
    pivot = array.pop(selectPivotLocation(array))
    lesser = [x for x in array if x < pivot]
    greater = [x for x in array if x >= pivot]
    return quickSort(lesser) + [pivot] + quickSort(greater)

def merge(left, right):
    result = []
    lp, rp = 0, 0
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[j]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    result += left[lp:]
    result += right[rp:]
    return result

def mergeSort(array):
    if len(array) <= 1:
        return array
        middle = int(len(array)/2)
        left = mergeSort(array[:middle])
        right = mergeSort(array[middle:])
        return merge(left, right)
