import sys

def insertion_sort(array, n): 
    if n == 1:
        return [array[0]]
    
    sorted_previous = insertion_sort(array, n-1)
    key = array[n-1]
    j = len(sorted_previous)

    while j >= 1 and sorted_previous[j-1] > key:
        j -= 1
    return sorted_previous[0:j] + [key] + sorted_previous[j:]

    


array = sys.argv[1:]
array = list(map(int, array))
sorted_array = insertion_sort(array, len(array))
print(' '.join(map(str, sorted_array)))
