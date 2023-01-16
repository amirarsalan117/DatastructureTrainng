def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr



numbers = [9,8,4,5,6,7,3,2,1]
print('unsorted numbers array', numbers)
numbers = selectionSort(numbers)
print('sorted numbers array:',numbers)