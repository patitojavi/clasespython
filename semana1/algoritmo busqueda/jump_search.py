

def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)

    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return -1


""" Jump Search es un algoritmo eficiente para listas ordenadas, con una complejidad de tiempo de O(√n), donde "n" es la longitud de la lista. 
Sin embargo, requiere que la lista esté ordenada previamente. """
