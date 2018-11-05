def quicksort(arr):
    if (len(arr) <= 1):
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


foo = [123, 25, 78, 4546, 753, 159, 852, 145, 652, 657]
print(quicksort(foo))
