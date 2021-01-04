import sys
# insert
# shift_up - needed for insert / swap
# get_max - returns the max item, without removing it
# get_size() - return number of elements stored
# is_empty() - returns true if heap contains no elements
# extract_max - returns the max item, removing it
# shift_down - needed for extract_max
# remove(i) - removes item at index x
# heapify - create a heap from an array of elements, needed for heap_sort
# heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap or min heap

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2   

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current =  self.size

        while(self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def get_max(self):
        return self.Heap[1]

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    # def extract_max(self):
    # def remove(self, pos):
    # def heapify(self):
    # def heap_sort(self):

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1])) 



maxHeap = MaxHeap(15) 

maxHeap.insert(5) 
maxHeap.insert(3) 
maxHeap.insert(17) 
maxHeap.insert(10) 
maxHeap.insert(84) 
maxHeap.insert(19) 
maxHeap.insert(6) 
maxHeap.insert(22) 
maxHeap.insert(9) 

# maxHeap.Print()

print(maxHeap.get_max())