class heap(object):
    HEAP_SIZE = 10
    def __init__(self):
        self.heap = [0]*heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self,item):
        if self.isFull():
            print('Heap is full')
            return
        self.currentPosition += 1
        self.heap[self.currentPosition] = item
        self.fixup(self.currentPosition)

    def isFull(self):
        if self.currentPosition == heap.HEAP_SIZE:
            return True
        else:
            return False

    def fixup(self,index):
        parentIndex = int((index-1)/2)
        while parentIndex >= 0  and self.heap[parentIndex] < self.heap[index]:
            self.heap[index],self.heap[parentIndex] = self.heap[parentIndex],self.heap[index]
            index=parentIndex
            parentIndex = int((index-1)/2)

    def getMax(self):
        result = self.heap[0]
        self.currentPosition = self.currentPosition-1
        self.heap[0] = self.heap[self.currentPosition]
        del self.heap[self.currentPosition + 1 ]
        self.fixDown(0,-1)
        return result

    def fixDown(self,index, upto):
        if index < 0:
            upto = self.currentPosition
        while index <= upto:
            leftChild = 2 * index + 1


