


def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

""" 
La búsqueda binaria es eficiente y tiene una complejidad de tiempo de O(log n), donde "n" es la longitud de la lista.  """