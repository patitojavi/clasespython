


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1  


        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



""" El algoritmo de inserción tiene una complejidad de tiempo de O(n^2) en el peor caso, pero es eficiente para listas pequeñas o casi ordenadas. """