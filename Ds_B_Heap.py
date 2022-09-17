class MinHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def GetParentIndex(self,index):
        return (index - 1) //2
    
    def GetLeftChild(self,index):
        return 2 * index + 1

    def GetRightChild(self,index):
        return 2 * index + 2
    
    def hasParent(self,index):
        return self.GetParentIndex(index) >= 0
    
    def hasLeftChild(self,index):
        return self.GetLeftChild(index) < self.size
    
    def hasRightChild(self,index):
        return self.getRightChild(index) > self.size
    
    def parent(self,index):
        return self.storage[self.GetParentIndex(index)]
    
    def left_child(self,index):
        return self.storage[self.hasLeftChild(index)]
    
    def right_child(self,index):
        return self.storage[self.GetRightChild(index)]
    
    def isFull(self):
        return self.size == self.storage
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
    # def insert(self, data):
    #     if self.isFull():
    #         raise Exception("Maximum Capacity Has Been Reach")
    #     self.storage[self.size] = data
    #     self.size += 1
    #     self.heapifyUp()
    
    # def heapifyUp(self):
    #     index = self.size - 1
    #     while self.hasParent(index) and self.parent(index) > self.storage[index]:
    #         self.swap(self.GetParentIndex(index), index)
    #         index = self.GetParentIndex(index)

    ''' Recursively '''
    def insert(self, data):
        if self.isFull():
            raise Exception("Maximum Capacity Has Been Reach")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)
    
    def remove(self):
        if self.size == 0:
            raise Exception("Maximum Capacity Has Been Reach")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size -1]
        self.size -= 1
        self.heapifyDown()
        return data
    
    def heapifyUp(self, index):
        # index = self.size - 1
        if (self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.GetParentIndex(index), index)
            self.heapifyUp(self.GetParentIndex(index))
    
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.GetLeftChild(index)
            if (self.hasRightChild(index) and self.right_child(index) < self.leftChild(index)):
                smallerChildIndex = self.GetRightChild(index)
            if (self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
class MaxHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0     

    ''' I'm Pretty rusty today, having a hard time absorbing imformation.
        I guess this is just a burn out and i could recover in a few day,
        why days?, well!!!, i'm still a student leaving in my parent property,
        so I'm putting time to learning to code and countinuing my day to day life.
        Ofcourse I'm Managing My time efficiently as well  '''