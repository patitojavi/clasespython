



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[len(arr)  // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + mid + quicksort(right)


""" El tiempo promedio de Quicksort es O(n log n), lo que lo hace más eficiente que el algoritmo de selección para listas grandes.
Sin embargo, su peor caso puede ser O(n^2) si se elige un pivote inadecuado, aunque esto es raro en la práctica si se elige el pivote de manera adecuada.
 """