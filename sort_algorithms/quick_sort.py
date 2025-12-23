# Quick Sort Algorithm
# Böl ve fethet yaklaşımı - pivot elemanı kullanır

def quick_sort(arr):
    """
    Quick Sort: Pivot elemanı seçer, küçükleri sola büyükleri sağa koyar.
    Zaman Karmaşıklığı: Ortalama O(n log n), En kötü O(n²)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test = [3, 6, 8, 10, 1, 2, 1]
    print(f"Sıralanmamış: {test}")
    print(f"Sıralanmış: {quick_sort(test)}")
