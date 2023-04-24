#Binary search
def binary_search(A, k):
    l = 0
    h = len(A) - 1
    while l <= h:
        mid = (l + h) // 2
        if A[mid] == k:
            return True
        elif A[mid] > k:
            h = mid - 1
        else:
            l = mid + 1
    return False

print(binary_search([1, 2, 3, 5, 8], 6)) # False
print(binary_search([1, 2, 3, 5, 8], 5)) # True

#'a' to the power 'b'
def power(a, b):
    return a ** b

print(power(3, 4))

#Bubble sort algorithm
def bubble_sort(nlist):
    n = len(nlist)
    for i in range(n):
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return nlist

list = [29,13,22,37,52,49,46,71,56]
sorted_data = bubble_sort(list)
print(sorted_data)

#Merge sort algorithm
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [29,13,22,37,52,49,46,71,56]
mergeSort(myList)
print(myList)

#Quick sort algorithm
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [29, 13, 22, 37, 52, 49, 46, 71, 56]
quick_sort(array, 0, len(array) - 1)
print(array)
