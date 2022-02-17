def binary(array, target):
    
    left = 0
    right = len(array) - 1
    
    while left <= right:
        
        middle = (left + right) // 2
        
        if array[middle] == target:
            
            return middle
        
        elif target < array[middle]:
            
            right = middle - 1
            
        else:
            
            left = middle + 1
            
    return -1
