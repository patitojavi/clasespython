

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1


mi_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento_buscado = 13
resultado = interpolation_search(mi_lista, elemento_buscado)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")
