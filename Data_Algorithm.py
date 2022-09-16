""" Purmutation """
def prefix_max(A,i):
    """ Return index of maximum  in A[:i + 1]"""
    if i > 0:
        """ Recursive """
        j = prefix_max(A, i-1)
        if A[i] < j[i]:
            return j
        return i

""" Selection Sort """
def selection_sort(A, i = None):
    """ Sort A[i + 1] """
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i - 1)

""" Merge Function """
def merge(L, R, A, i, j, a, b):
    ''' Merge Sorted L[:i] and R[:j] into A[a:b] '''
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L [i - 1]
            i =  i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
            merge(L, R, A, i, j, a, b - 1)
            
""" Merge Sort """
def merge_sort(A, a = 0, i = None):
    ''' Sort A[a:b] '''
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:b], A[c:b]
        merge(L, R, A, len(L), len(R), a,b)

''' Linked List Implementation '''

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return      
          
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_value(self, data):
        if self.head.data is None:
            print("Linked List Is Empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        
        
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("You need to rethink your life")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
                
            itr = itr.next
            count += 1
            
        
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        
    def print(self):
        if self.head == None:
            print("LinkList Is Empty")
            return
        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

''' Doubly Linked List '''
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

''' Tree Implementation '''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
        root = TreeNode("Electronics")

        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Surface"))
        laptop.add_child(TreeNode("Thinkpad"))

        cellphone = TreeNode("Cell Phone")
        cellphone.add_child(TreeNode("iPhone"))
        cellphone.add_child(TreeNode("Google Pixel"))
        cellphone.add_child(TreeNode("Vivo"))

        tv = TreeNode("TV")
        tv.add_child(TreeNode("Samsung"))
        tv.add_child(TreeNode("LG"))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        root.print_tree()

if __name__ == '__main__':
    pass
    #build_product_tree()

    "Im The Stupidest Person Alive :("

""" Binary Tree """

class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def appended(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.appended(data)
            else:
                self.left = Binary_Tree(data)
        else:
            if self.right:
                self.right.appended(data)
            else:
                self.right = Binary_Tree(data)
    
    def search(self, data):
        # searching recursively
        if self.data == data:
            return True
        
        elif data < self.data:
            # it might be in left subtree
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        elif data > self.data:
            # it might be in right subtree
            if self.right:
                return self.right.search(data)
            else:
                return False
        
    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    

def build_product_tree(element):
    root = Binary_Tree(element[0])

    for i in range(1, len(element)):
        root.appended(element[i])
    
    return root

if __name__ == '__main__':
    numbers_tree = build_product_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.search(1))
    print(numbers_tree.find_max())
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    print(numbers_tree.calculate_sum())

    ''' My head is starting to work, but!!! yeah still stupid
        or maybe i just woke up and that's why my head is working
                                                                '''



