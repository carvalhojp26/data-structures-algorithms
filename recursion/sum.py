def recursive_sum(arr):
    if len(arr) == 0 :
        return 0
    elif len(arr) == 1 :
        return arr[0]
    else :
        newArr = arr[1:]
        return arr[0] + recursive_sum(newArr)

print(recursive_sum([1, 3, 5]))