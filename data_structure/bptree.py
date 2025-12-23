# B+ Tree (B Plus Tree)
# Veritabanlarında sıklıkla kullanılan dengeli ağaç yapısı.
# Tüm veriler YAPRAK düğümlerde tutulur ve yapraklar birbirine bağlıdır.

class BPlusNode:
    """
    B+ Tree Düğümü:
    - keys: Bu düğümdeki anahtarlar (sıralı)
    - children: Çocuk düğümler (iç düğümler için)
    - values: Değerler (sadece yapraklar için)
    - is_leaf: Yaprak mı değil mi
    - next: Sonraki yaprak düğüm (yapraklar zincirleme bağlı)
    """
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.values = []  # Sadece yapraklarda kullanılır
        self.is_leaf = is_leaf
        self.next = None  # Yapraklar arası bağlantı


class BPlusTree:
    """
    B+ Tree:
    - order (derece): Her düğümün max kaç çocuğu olabileceği
    - Tüm değerler yapraklarda tutulur
    - Yapraklar linked list gibi birbirine bağlıdır (range query için harika)
    """
    def __init__(self, order=3):
        self.root = BPlusNode(is_leaf=True)
        self.order = order  # Max çocuk sayısı

    def search(self, key):
        """Bir anahtarı arar, bulursa değerini döndürür."""
        node = self._find_leaf(key)
        
        for i, k in enumerate(node.keys):
            if k == key:
                return node.values[i]
        return None

    def _find_leaf(self, key):
        """Verilen anahtar için uygun yaprak düğümü bulur."""
        node = self.root
        
        while not node.is_leaf:
            # Hangi çocuğa gideceğimizi bul
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        
        return node

    def insert(self, key, value):
        """Ağaca yeni anahtar-değer çifti ekler."""
        leaf = self._find_leaf(key)
        
        # Yaprak içinde doğru pozisyonu bul
        i = 0
        while i < len(leaf.keys) and leaf.keys[i] < key:
            i += 1
        
        # Anahtar zaten varsa değeri güncelle
        if i < len(leaf.keys) and leaf.keys[i] == key:
            leaf.values[i] = value
            return
        
        # Yeni anahtar-değer ekle
        leaf.keys.insert(i, key)
        leaf.values.insert(i, value)
        
        # Yaprak doluysa böl
        if len(leaf.keys) >= self.order:
            self._split_leaf(leaf)

    def _split_leaf(self, leaf):
        """Dolu yaprağı ikiye böler."""
        mid = len(leaf.keys) // 2
        
        # Yeni yaprak oluştur
        new_leaf = BPlusNode(is_leaf=True)
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.values = leaf.values[mid:]
        
        # Eski yaprağı küçült
        leaf.keys = leaf.keys[:mid]
        leaf.values = leaf.values[:mid]
        
        # Yapraklar arası bağlantı
        new_leaf.next = leaf.next
        leaf.next = new_leaf
        
        # Promosyon anahtarı (yeni yaprağın ilk anahtarı yukarı çıkar)
        promotion_key = new_leaf.keys[0]
        
        # Üst düğüme ekle
        self._insert_in_parent(leaf, promotion_key, new_leaf)

    def _insert_in_parent(self, left_node, key, right_node):
        """Bölünmeden sonra üst düğüme anahtar ekler."""
        # Kök bölündüyse yeni kök oluştur
        if left_node == self.root:
            new_root = BPlusNode(is_leaf=False)
            new_root.keys = [key]
            new_root.children = [left_node, right_node]
            self.root = new_root
            return
        
        # Üst düğümü bul ve anahtarı ekle
        parent = self._find_parent(self.root, left_node)
        
        # Doğru pozisyonu bul
        i = 0
        while i < len(parent.keys) and parent.keys[i] < key:
            i += 1
        
        parent.keys.insert(i, key)
        parent.children.insert(i + 1, right_node)
        
        # Üst düğüm doluysa onu da böl
        if len(parent.keys) >= self.order:
            self._split_internal(parent)

    def _split_internal(self, node):
        """Dolu iç düğümü böler."""
        mid = len(node.keys) // 2
        promotion_key = node.keys[mid]
        
        # Yeni iç düğüm
        new_node = BPlusNode(is_leaf=False)
        new_node.keys = node.keys[mid + 1:]
        new_node.children = node.children[mid + 1:]
        
        # Eski düğümü küçült
        node.keys = node.keys[:mid]
        node.children = node.children[:mid + 1]
        
        # Üst düğüme ekle
        self._insert_in_parent(node, promotion_key, new_node)

    def _find_parent(self, current, child):
        """Bir düğümün üst düğümünü bulur."""
        if current.is_leaf or current == child:
            return None
        
        for i, c in enumerate(current.children):
            if c == child:
                return current
            if not c.is_leaf:
                result = self._find_parent(c, child)
                if result:
                    return result
        return None

    def print_tree(self):
        """Ağacı seviye seviye yazdırır."""
        if not self.root:
            print("Ağaç boş")
            return
        
        queue = [(self.root, 0)]
        current_level = 0
        
        print("B+ Tree Yapısı:")
        print("-" * 40)
        
        while queue:
            node, level = queue.pop(0)
            
            if level > current_level:
                print()
                current_level = level
            
            if node.is_leaf:
                print(f"[Yaprak: {node.keys}]", end=" ")
            else:
                print(f"[İç: {node.keys}]", end=" ")
            
            if not node.is_leaf:
                for child in node.children:
                    queue.append((child, level + 1))
        print()

    def range_query(self, start, end):
        """
        Aralık sorgusu - B+ Tree'nin en güçlü özelliği!
        Yapraklar birbirine bağlı olduğu için çok hızlı.
        """
        result = []
        leaf = self._find_leaf(start)
        
        while leaf:
            for i, key in enumerate(leaf.keys):
                if key > end:
                    return result
                if key >= start:
                    result.append((key, leaf.values[i]))
            leaf = leaf.next
        
        return result


# --- KULLANIM / TEST ---

if __name__ == "__main__":
    bpt = BPlusTree(order=3)

    print("B+ Tree'ye elemanlar ekleniyor...")
    data = [(10, "on"), (20, "yirmi"), (5, "beş"), (15, "onbeş"), 
            (25, "yirmibeş"), (30, "otuz"), (12, "oniki")]
    
    for key, value in data:
        bpt.insert(key, value)
        print(f"  Eklendi: {key} -> {value}")
    
    print()
    bpt.print_tree()
    
    print("\n--- Arama Testleri ---")
    print(f"15 ara: {bpt.search(15)}")
    print(f"25 ara: {bpt.search(25)}")
    print(f"100 ara: {bpt.search(100)}")
    
    print("\n--- Aralık Sorgusu (Range Query) ---")
    print(f"10-25 arası: {bpt.range_query(10, 25)}")
