# Merge Sort Algorithm
# Böl ve fethet yaklaşımı - listeyi ikiye böler

def merge_sort(arr):
    """
    Merge Sort: Listeyi ikiye böler, sıralar ve birleştirir.
    Zaman Karmaşıklığı: O(n log n) - her durumda stabil
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """İki sıralı listeyi birleştirir."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test = [38, 27, 43, 3, 9, 82, 10]
    print(f"Sıralanmamış: {test}")
    print(f"Sıralanmış: {merge_sort(test)}")
