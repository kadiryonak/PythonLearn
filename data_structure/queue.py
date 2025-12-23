# Queue (FIFO - First In First Out)
# Linked list kullanarak queue (kuyruk) yapısı oluşturulmuştur.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  # Kuyruğun önü (çıkış noktası)
        self.rear = None   # Kuyruğun arkası (giriş noktası)

    def is_empty(self):
        """Kuyruk boş mu kontrol et."""
        return self.front is None

    def enqueue(self, data):
        """Kuyruğa eleman ekle (arkadan)."""
        new_node = Node(data)
        
        if self.rear is None:
            # Kuyruk boşsa, hem front hem rear bu düğüm olur
            self.front = new_node
            self.rear = new_node
        else:
            # Yeni düğümü arkaya ekle
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Kuyruktan eleman çıkar (önden)."""
        if self.is_empty():
            return None
        
        value = self.front.data
        self.front = self.front.next
        
        # Eğer kuyruk boşaldıysa rear'ı da None yap
        if self.front is None:
            self.rear = None
        
        return value

    def peek(self):
        """Öndeki elemanı göster ama çıkarma."""
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        """Kuyruktaki eleman sayısını döndür."""
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """Kuyruğu ekrana yazdır."""
        if self.is_empty():
            print("Kuyruk boş")
            return
        
        current = self.front
        print("Kuyruk: ", end="")
        while current:
            print(f"{current.data}", end=" <- ")
            current = current.next
        print("(arka)")


if __name__ == "__main__":

    q = Queue()

    print("Kuyruğa ekleniyor: 5, 10, 15, 20")
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    q.enqueue(20)

    q.display()  # 5 <- 10 <- 15 <- 20 <- (arka)

    print(f"\nÖndeki eleman (peek): {q.peek()}")
    print(f"Kuyruk boyutu: {q.size()}")

    print("\nDequeue işlemleri (FIFO):")
    print(f"  Çıkan: {q.dequeue()}")  # 5 (ilk giren)
    print(f"  Çıkan: {q.dequeue()}")  # 10
    print(f"  Çıkan: {q.dequeue()}")  # 15

    q.display()  # 20 <- (arka)

    print(f"\nKuyruk boyutu: {q.size()}")
