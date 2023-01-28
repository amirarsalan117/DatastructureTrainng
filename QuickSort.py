def QuickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)



numbers = [9,7,8,6,4,5,3,2,5,1,6,7,8,4,5,98]
new_numbers = QuickSort(numbers)
print(new_numbers)