# Binary Tree (İkili Ağaç) ve Binary Search Tree (İkili Arama Ağacı)
# Her düğümün en fazla 2 çocuğu olabilir: Sol (left) ve Sağ (right)

class Node:
    """
    Ağaç Düğümü:
    - data: Düğümün taşıdığı değer
    - left: Sol çocuk düğüm (daha küçük değerler buraya gider)
    - right: Sağ çocuk düğüm (daha büyük değerler buraya gider)
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) - İkili Arama Ağacı:
    - Sol alt ağaçtaki tüm değerler, kök düğümden KÜÇÜKTÜR.
    - Sağ alt ağaçtaki tüm değerler, kök düğümden BÜYÜKTÜR.
    """
    def __init__(self):
        self.root = None  # Ağacın kökü (başlangıçta boş)

    def insert(self, data):
        """Ağaca yeni bir değer ekler."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Yardımcı recursive (özyinelemeli) ekleme fonksiyonu."""
        if data < node.data:
            # Küçükse sola git
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            # Büyükse veya eşitse sağa git
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        """Ağaçta bir değeri arar, bulursa True döner."""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """Yardımcı arama fonksiyonu."""
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    # --- AĞACI GEZİNME (TRAVERSAL) YÖNTEMLERİ ---

    def inorder(self, node):
        """
        Inorder Traversal (Sol -> Kök -> Sağ)
        BST için bu SIRALI çıktı verir!
        """
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """
        Preorder Traversal (Kök -> Sol -> Sağ)
        Ağacı kopyalamak için kullanışlıdır.
        """
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """
        Postorder Traversal (Sol -> Sağ -> Kök)
        Ağacı silmek için kullanışlıdır.
        """
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# --- KULLANIM / TEST ---

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Elemanları ekleyelim
    #         50
    #        /  \
    #       30   70
    #      / \   / \
    #     20 40 60 80
    
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Inorder (Sıralı): ", end="")
    bst.inorder(bst.root)  # Çıktı: 20 30 40 50 60 70 80
    print()

    print("Preorder: ", end="")
    bst.preorder(bst.root)  # Çıktı: 50 30 20 40 70 60 80
    print()

    print("Postorder: ", end="")
    bst.postorder(bst.root)  # Çıktı: 20 40 30 60 80 70 50
    print()

    # Arama testi
    print(f"\n40 ağaçta var mı? {bst.search(40)}")  # True
    print(f"100 ağaçta var mı? {bst.search(100)}")  # False
