class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_the_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_the_end(self, data):  
        if self.head is None:
            node = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_beginning(data)
    
    def remove_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

    
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
dataa = ['as', 'he', 'she', 'him']
if __name__ == '__main__':
    l = LinkedList()

    l.remove_value(dataa)
    l.print()
