
''' BUBBLE SORT '''
array = [1, 5, 8, 6, 9, 14, 16, 711, 5123, 125156]

for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]


print(array)

''' BUBBLE SORT '''


''' INSERTION SORT '''

array = [1, 78, 8, 6, 9, 14, 16, 711, 3, 5123, 125156]

for i in range(1, len(array)):
    temp = array[i]
    j = i - 1
    while array[j] > temp:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = temp

print(array)

''' INSERTION SORT '''

''' SELECTION SORT '''

array = [1, 78, 8, 6, 9, 14, 16, 711, 3, 5123, 125156]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
''' SELECTION SORT '''

''' MERGE SORT '''
array = [1, 78, 8, 6, 9, 14, 16, 711, 3, 5123, 125156]


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):  
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  
    result += right[j:]  

    return result


def sort(array):
    if len(array) < 2:
        return array  
    mid = len(array) // 2
    left = sort(array[:mid])  
    right = sort(array[mid:])
    return merge(left, right)


print(sort(array))
''' MERGE SORT '''

''' QUICK SORT '''
array = [1, 78, 8, 6, 9, 14, 16, 711, 3, 5123, 125156]


def quick(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x <= pivot]  
    right = [x for x in array[1:] if x > pivot]  
    return quick(left) + [pivot] + quick(right)


''' QUICK SORT '''

''' HEAP SORT '''
array = [1, 78, 8, 6, 9, 14, 16, 711, 3, 5123, 125156]

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2


    if l < n and arr[i] < arr[l]:
        largest = l


    if r < n and arr[largest] < arr[r]:
        largest = r


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap


        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

   
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)




heapSort(array)
n = len(array)
print(array)
''' HEAP SORT '''

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
