# Selection Sort Algorithm
# Listedeki en küçük elemanı bulur ve başa koyar

def selection_sort(arr):
    """
    Selection Sort: Her adımda sıralanmamış kısımdan en küçük elemanı bulur
    ve doğru konuma yerleştirir.
    Zaman Karmaşıklığı: O(n²)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    test = [64, 25, 12, 22, 11]
    print(f"Sıralanmamış: {test}")
    print(f"Sıralanmış: {selection_sort(test.copy())}")
