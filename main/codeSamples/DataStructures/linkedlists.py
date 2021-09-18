class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def __repr__(self):
        return self.data
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_data(self, data=None):
        self.data = data
    
    def set_next(self, next_node=None):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current_head = self.head
        count = 0
        while current_head:
            current_head = current_head.get_next()
            count += 1
        return count
    
    def search(self, data):
        print("Searching: {}".format(data))
        current_head = self.head
        found = False
        while current_head and found is False:
            if current_head.get_data() == data:
                found = True
                print("Found: {}".format(data))
            else:
                current_head = current_head.get_next()
        if current_head is None:
            raise ValueError("Data not in list")
        return current_head

    def delete(self, data):
        print("Deleting: {}".format(data))
        current_head = self.head
        previous_head = None
        found = False
        while current_head and found is False:
            if current_head.get_data() == data:
                found = True

            else:
                previous_head = current_head
                current_head = current_head.get_next()
        if current_head is None:
            raise ValueError("Data not in list")
        if previous_head is None:
            self.head = current_head.get_next()
        else:
            previous_head.set_next(current_head.get_next())

    def printLL(self):
        current = self.head
        data = "Current List: "
        while current:
            data += str(current.data) + " "
            current = current.get_next()
        print(data)

if __name__ == '__main__':
    LL = LinkedList()
    LL.insert(3)
    LL.insert(6)
    LL.insert(4)
    LL.insert(12)
    LL.insert(19)
    LL.printLL()
    LL.delete(4)
    LL.printLL()
    LL.delete(12)
    LL.printLL()
    LL.search(6)
    LL.search(12)