class PriorityQueue:
    def __init__(self):
        self.array = []
        self.heap_size = 0
    

    def _sift_up(self, index):
        parent_node = index//2 - 1
        if index == 1 or self.array[index-1] <= self.array[parent_node]:
            return
        self.array[index-1], self.array[parent_node] = self.array[parent_node], self.array[index-1]
        self._sift_up(parent_node)


    def _heapify(self, array, root):

        heap_size = len(array[root:])
        root += 1
        left = root*2
        right = root*2+1
        largest = root

        if left<=heap_size and array[left-1] > array[largest-1]:
            largest = left
        if right<=heap_size and array[right-1] > array[largest-1]:
            largest = right
        if largest != root:
            array[root-1], array[largest-1] = array[largest-1], array[root-1]
            self._heapify(array, largest-1)
        

    def insert(self, element):
        self.array.append(element)
        self.heap_size += 1
        self._sift_up(self.heap_size)
        return

    def extract_max(self):
        max_element = self.array[0]
        self.array[0] = self.array.pop(self.heap_size-1)
        self.heap_size -= 1
        self._heapify(self.array, 0)
        return max_element

if __name__ == "__main__":
    
    n = int(input())

    a = PriorityQueue()

    for i in range(n):
        try:
            action, element = input().split(" ")
            a.insert(element)
        except ValueError:
            max_element = a.extract_max()
            print(max_element)