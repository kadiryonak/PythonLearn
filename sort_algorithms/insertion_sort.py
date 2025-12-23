# Insertion Sort Algorithm
# Her elemanı sıralı kısma doğru yere yerleştirir

def insertion_sort(arr):
    """
    Insertion Sort: Her elemanı sıralı kısımda doğru konuma yerleştirir.
    Zaman Karmaşıklığı: O(n²) - küçük listeler için verimli
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test = [12, 11, 13, 5, 6]
    print(f"Sıralanmamış: {test}")
    print(f"Sıralanmış: {insertion_sort(test.copy())}")
