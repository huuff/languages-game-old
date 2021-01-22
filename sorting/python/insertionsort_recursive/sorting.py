import sys

def insertion_sort(arr, n): 
    if n == 1:
        return arr[0]
    
    sorted_previous = insertion_sort(arr, n-1)
    key = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > key:
        j -= 1
    return arr[0:j] + [key] + arr[j+1:]

    


arr = sys.argv[1:]
arr = list(map(int, arr))
insertion_sort(arr, len(arr))
print(' '.join(map(str, arr)))
