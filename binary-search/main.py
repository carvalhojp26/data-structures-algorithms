def binary_search(arr, item) :
    low = 0
    high = len(arr) - 1

    while low <= high : 
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item :
            return guess
        
        if guess < item :
            low = mid + 1
    
        if guess > item :
            high = mid - 1
    
        
    return None

print(binary_search([1, 3, 5, 7, 9], 3))