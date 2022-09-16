class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Tree(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.left = Binary_Tree(data)
    
    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()
    
    def find_min(self):
        if self.right is None:
            return self.data
        
        return self.left.find_max()
    
    def search(self):
        if self.data == data:
            return True
        
        elif self.data < data:
            if self.left:
                return self.left.search()
            else:
                return False
        
        elif self.data > data:
            if self.right:
                return self.right.search()
            else:
                return False
        
    def in_order_traversal(self):
        element = []
        
        if self.left:
            element += self.left.in_order_traversal()
        
        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()
        
        return element
    
    def remove(self, data):
        pass
        

def build_product_tree(element):
    root = Binary_Tree(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])
    
    return root