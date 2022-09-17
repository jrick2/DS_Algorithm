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
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
            max_val = self.right.find_max()
            self.data = max_val
            self.right = self.right.delete(max_val)


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
    # numbers_tree = build_product_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print(numbers_tree.search(1))
    # print(numbers_tree.find_max())
    # numbers_tree.delete(20)
    # print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    # print(numbers_tree.calculate_sum())
    pass

    ''' My head is starting to work, but!!! yeah still stupid
        or maybe i just woke up and that's why my head is working
                                                                '''