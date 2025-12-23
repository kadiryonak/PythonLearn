


class Node:

    def __init__(self,data):
        self.data = data # Bu yapıda tutacağımız data
        self.next = None # Bu yapıda tutacağımız sonraki node



class LinkedList:
    # Linked list sınıf yapısı
    def __init__(self):
        self.head = None
    
    def append(self,data):
        # Listeye ekleme fonksiyonu
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    
    def print_list(self):
        # Listeyi ekrana yazdırma  fonksiyonu
        start_node = self.head
        while start_node:
            print(start_node.data)
            start_node = start_node.next


    def delete_data(self,value):
        # Data silme fonksiyonu
        current = self.head
        prev = None


        if current.data == value:
            self.head = current.next
            current = None
            print("Burası Delete Data Metodu")
            return self.print_list()

        while current and current.data !=value:
            prev = current
            current = current.next


            
            

        
        


if __name__ == "__main__":

    linklist = LinkedList()


    linklist.append(2)
    linklist.append(11)
    linklist.append(3)
    linklist.append(7)
    linklist.append(5)
    linklist.append(6)
    linklist.append(16)
    linklist.append(8)
    linklist.append(9)
    linklist.append(10)


    linklist.print_list()

    linklist.delete_data(2)

    linklist.print_list()
