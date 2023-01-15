def binarySearch(array , item):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if item == array[mid]:
            return mid
        elif array[mid] < item:
            low = mid +1
        else:
            high = mid -1
    return -1
    
    
numbers = [1,2,3,4,5,6,7,8]
#function return the position of 4 that is in index 3
print(binarySearch(numbers ,4))        
# function return -1 becuse we dont have 99 in arrays
print(binarySearch(numbers , 99))
    