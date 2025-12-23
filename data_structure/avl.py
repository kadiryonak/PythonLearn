# AVL Tree (Kendini Dengeleyen İkili Arama Ağacı)
# Normal BST'den farkı: Otomatik olarak dengelenir, böylece arama hep hızlı kalır.
# Her düğümün "height" (yükseklik) değeri tutulur ve denge faktörü kontrol edilir.

class AVLNode:
    """
    AVL Düğümü:
    - data: Değer
    - left/right: Sol ve sağ çocuklar
    - height: Bu düğümün yüksekliği (yapraklar için 1)
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Yeni düğüm her zaman yaprak olarak başlar


class AVLTree:
    """
    AVL Tree - Adelson-Velsky and Landis Ağacı:
    - Denge Faktörü = Sol Yükseklik - Sağ Yükseklik
    - Denge faktörü -1, 0, veya 1 olmalı. Aksi halde rotasyon yapılır.
    """
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        """Düğümün yüksekliğini döndürür (None için 0)."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Denge faktörünü hesaplar."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        """
        Sağa Döndürme (Right Rotation):
        Sol-sol dengesizliğinde kullanılır.
        
             y                x
            / \             /   \
           x   T3   -->    T1    y
          / \                   / \
         T1  T2                T2  T3
        """
        x = y.left
        T2 = x.right

        # Döndürme işlemi
        x.right = y
        y.left = T2

        # Yükseklikleri güncelle
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x  # Yeni kök

    def _left_rotate(self, x):
        """
        Sola Döndürme (Left Rotation):
        Sağ-sağ dengesizliğinde kullanılır.
        
           x                    y
          / \                 /   \
         T1  y     -->       x     T3
            / \             / \
           T2  T3          T1  T2
        """
        y = x.right
        T2 = y.left

        # Döndürme işlemi
        y.left = x
        x.right = T2

        # Yükseklikleri güncelle
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y  # Yeni kök

    def insert(self, data):
        """Ağaca yeni değer ekler ve dengeleme yapar."""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Recursive ekleme ve dengeleme."""
        # 1. Normal BST ekleme
        if not node:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)

        # 2. Yüksekliği güncelle
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 3. Denge faktörünü kontrol et
        balance = self._get_balance(node)

        # 4. Dengesizlik varsa rotasyon yap (4 durum var)

        # Sol-Sol Durumu (Left-Left)
        if balance > 1 and data < node.left.data:
            return self._right_rotate(node)

        # Sağ-Sağ Durumu (Right-Right)
        if balance < -1 and data > node.right.data:
            return self._left_rotate(node)

        # Sol-Sağ Durumu (Left-Right)
        if balance > 1 and data > node.left.data:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Sağ-Sol Durumu (Right-Left)
        if balance < -1 and data < node.right.data:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def inorder(self, node):
        """Inorder gezinme (sıralı çıktı verir)."""
        if node:
            self.inorder(node.left)
            print(f"{node.data}(h={node.height})", end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """Preorder gezinme (ağaç yapısını gösterir)."""
        if node:
            print(f"{node.data}(h={node.height})", end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


# --- KULLANIM / TEST ---

if __name__ == "__main__":
    avl = AVLTree()

    # Sıralı ekleme - Normal BST'de bu çok dengesiz olurdu!
    # Ama AVL kendini dengeler
    print("Elemanlar ekleniyor: 10, 20, 30, 40, 50, 25")
    
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)

    #       30
    #      /  \
    #     20   40
    #    / \     \
    #   10  25   50

    print("\nPreorder (Yapı): ", end="")
    avl.preorder(avl.root)
    print()

    print("Inorder (Sıralı): ", end="")
    avl.inorder(avl.root)
    print()

    print("\nKök düğüm:", avl.root.data)
    print("Denge faktörü (kök):", avl._get_balance(avl.root))
