# Stack (LIFO - Last In First Out)
# Linked list kullanarak stack yapısı oluşturulmuştur.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.data
        self.top = self.top.next
        return value


if __name__ == "__main__":

     a = Stack()
     a.push(5)
     a.push(10)
     a.push(15)
     print(a.pop())
     print(a.pop())
     print(a.pop())